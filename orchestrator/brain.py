import logging
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from typing_extensions import TypedDict

from agents import ResearchAgent, AnalysisAgent, CreativeAgent, AgentResponse
from .selector import AgentSelector

logger = logging.getLogger(__name__)


class AgentState(TypedDict):
    """State for the agent orchestration graph"""
    query: str
    selected_agents: List[str]
    current_agent_index: int
    agent_responses: List[Dict[str, Any]]
    final_response: str
    conversation_history: List[BaseMessage]
    context: Dict[str, Any]


@dataclass
class OrchestratorResult:
    """Result from the orchestrator"""
    response: str
    agents_used: List[str]
    agent_details: List[Dict[str, Any]]
    success: bool
    error: Optional[str] = None


class LangGraphBrain:
    """
    LangGraph-based orchestrator that serves as the brain of the system
    Intelligently routes queries to appropriate Dify agents
    """
    
    def __init__(self):
        self.selector = AgentSelector()
        
        # Initialize agents
        self.agents = {
            "research": ResearchAgent(),
            "analysis": AnalysisAgent(),
            "creative": CreativeAgent()
        }
        
        # Build the graph
        self.graph = self._build_graph()
        
        logger.info("LangGraph Brain initialized with 3 agents")
    
    def _build_graph(self) -> StateGraph:
        """Build the LangGraph orchestration graph"""
        
        workflow = StateGraph(AgentState)
        
        # Add nodes
        workflow.add_node("select_agents", self._select_agents_node)
        workflow.add_node("execute_agent", self._execute_agent_node)
        workflow.add_node("aggregate_results", self._aggregate_results_node)
        
        # Define edges
        workflow.add_edge(START, "select_agents")
        workflow.add_edge("select_agents", "execute_agent")
        workflow.add_conditional_edges(
            "execute_agent",
            self._should_continue,
            {
                "continue": "execute_agent",
                "aggregate": "aggregate_results"
            }
        )
        workflow.add_edge("aggregate_results", END)
        
        return workflow.compile()
    
    def _select_agents_node(self, state: AgentState) -> AgentState:
        """Node: Select which agents to use"""
        query = state["query"]
        
        logger.info("Selecting agents for query...")
        selected_agents = self.selector.select_agents(query)
        
        logger.info(f"Selected agents: {selected_agents}")
        
        state["selected_agents"] = selected_agents
        state["current_agent_index"] = 0
        state["agent_responses"] = []
        
        return state
    
    def _execute_agent_node(self, state: AgentState) -> AgentState:
        """Node: Execute the current agent"""
        selected_agents = state["selected_agents"]
        current_index = state["current_agent_index"]
        agent_responses = state["agent_responses"]
        
        if current_index >= len(selected_agents):
            return state
        
        agent_key = selected_agents[current_index]
        agent = self.agents.get(agent_key)
        
        if not agent or not agent.is_available():
            logger.warning(f"Agent {agent_key} not available, skipping")
            state["current_agent_index"] += 1
            return state
        
        # Prepare query with context from previous agents
        query = state["query"]
        context = state.get("context", {})
        
        # Add previous agent responses as context
        if agent_responses:
            context["previous_results"] = [
                {
                    "agent": resp["agent_name"],
                    "response": resp["content"][:500]  # Limit context size
                }
                for resp in agent_responses
            ]
        
        # Execute agent
        logger.info(f"Executing {agent.agent_name}...")
        response = agent.execute(query, context=context)
        
        # Store response
        agent_responses.append({
            "agent_name": response.agent_name,
            "content": response.content,
            "success": response.success,
            "metadata": response.metadata,
            "error": response.error
        })
        
        state["agent_responses"] = agent_responses
        state["current_agent_index"] = current_index + 1
        
        return state
    
    def _should_continue(self, state: AgentState) -> str:
        """Decide whether to continue executing agents or aggregate results"""
        current_index = state["current_agent_index"]
        selected_agents = state["selected_agents"]
        
        if current_index >= len(selected_agents):
            return "aggregate"
        return "continue"
    
    def _aggregate_results_node(self, state: AgentState) -> AgentState:
        """Node: Aggregate results from all agents"""
        agent_responses = state["agent_responses"]
        
        if not agent_responses:
            state["final_response"] = "No agents were able to process the query."
            return state
        
        # If single agent, return its response directly
        if len(agent_responses) == 1:
            response = agent_responses[0]
            if response["success"]:
                state["final_response"] = response["content"]
            else:
                state["final_response"] = f"Error: {response.get('error', 'Unknown error')}"
            return state
        
        # Multiple agents - combine their responses
        successful_responses = [r for r in agent_responses if r["success"]]
        
        if not successful_responses:
            errors = [r.get("error", "Unknown") for r in agent_responses]
            state["final_response"] = f"All agents failed. Errors: {', '.join(errors)}"
            return state
        
        # Create a structured response combining all agent outputs
        combined_response = []
        
        for i, response in enumerate(successful_responses, 1):
            agent_name = response["agent_name"]
            content = response["content"]
            
            if len(successful_responses) > 1:
                combined_response.append(f"## {agent_name} Response:\n{content}\n")
            else:
                combined_response.append(content)
        
        state["final_response"] = "\n".join(combined_response)
        
        return state
    
    def process_query(
        self, 
        query: str, 
        context: Optional[Dict[str, Any]] = None
    ) -> OrchestratorResult:
        """
        Process a user query through the agent system
        
        Args:
            query: User query
            context: Optional additional context
            
        Returns:
            OrchestratorResult with response and agent information
        """
        try:
            logger.info(f"Processing query: {query[:100]}...")
            
            # Initialize state
            initial_state: AgentState = {
                "query": query,
                "selected_agents": [],
                "current_agent_index": 0,
                "agent_responses": [],
                "final_response": "",
                "conversation_history": [HumanMessage(content=query)],
                "context": context or {}
            }
            
            # Run the graph
            final_state = self.graph.invoke(initial_state)
            
            # Extract results
            agent_responses = final_state["agent_responses"]
            agents_used = [r["agent_name"] for r in agent_responses if r["success"]]
            
            if not agents_used:
                return OrchestratorResult(
                    response="Unable to process query - no agents available",
                    agents_used=[],
                    agent_details=[],
                    success=False,
                    error="No agents available"
                )
            
            return OrchestratorResult(
                response=final_state["final_response"],
                agents_used=agents_used,
                agent_details=agent_responses,
                success=True
            )
            
        except Exception as e:
            logger.error(f"Error in orchestrator: {str(e)}", exc_info=True)
            return OrchestratorResult(
                response="An error occurred while processing your query",
                agents_used=[],
                agent_details=[],
                success=False,
                error=str(e)
            )
