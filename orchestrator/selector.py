import logging
from typing import List, Dict, Any
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from config import config

logger = logging.getLogger(__name__)


class AgentSelector:
    """
    Intelligent agent selector that analyzes queries and determines which agent(s) to use
    """
    
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            api_key=config.openai_api_key
        )
        
        self.agents_info = {
            "research": {
                "name": config.research_agent.name,
                "description": config.research_agent.description,
                "keywords": config.research_agent.keywords
            },
            "analysis": {
                "name": config.analysis_agent.name,
                "description": config.analysis_agent.description,
                "keywords": config.analysis_agent.keywords
            },
            "creative": {
                "name": config.creative_agent.name,
                "description": config.creative_agent.description,
                "keywords": config.creative_agent.keywords
            }
        }
    
    def select_agents(self, query: str) -> List[str]:
        """
        Select appropriate agent(s) for the query
        
        Args:
            query: User query
            
        Returns:
            List of agent names to use (in order of execution)
        """
        logger.info(f"Selecting agents for query: {query[:100]}...")
        
        # First, try keyword-based selection for speed
        keyword_agents = self._keyword_based_selection(query)
        
        # If keyword selection is confident (1 or 2 agents), use it
        if len(keyword_agents) <= 2:
            logger.info(f"Keyword-based selection: {keyword_agents}")
            return keyword_agents
        
        # Otherwise, use LLM for more nuanced selection
        llm_agents = self._llm_based_selection(query)
        logger.info(f"LLM-based selection: {llm_agents}")
        return llm_agents
    
    def _keyword_based_selection(self, query: str) -> List[str]:
        """Fast keyword-based agent selection"""
        query_lower = query.lower()
        selected = []
        scores = {}
        
        for agent_key, agent_info in self.agents_info.items():
            score = sum(1 for keyword in agent_info["keywords"] if keyword in query_lower)
            if score > 0:
                scores[agent_key] = score
        
        # Sort by score and select top agents
        sorted_agents = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        # Select agents with significant scores
        if sorted_agents:
            max_score = sorted_agents[0][1]
            for agent_key, score in sorted_agents:
                if score >= max_score * 0.5:  # At least 50% of max score
                    selected.append(agent_key)
        
        # Default to research if no clear match
        if not selected:
            selected = ["research"]
        
        return selected
    
    def _llm_based_selection(self, query: str) -> List[str]:
        """LLM-based agent selection for complex queries"""
        
        system_prompt = f"""You are an intelligent agent selector. Analyze the user's query and determine which agent(s) should handle it.

Available Agents:
1. Research Agent: {self.agents_info['research']['description']}
2. Analysis Agent: {self.agents_info['analysis']['description']}
3. Creative Agent: {self.agents_info['creative']['description']}

Rules:
- Select ONE agent for simple, focused tasks
- Select MULTIPLE agents (in sequence) for complex tasks that require different capabilities
- Order matters: agents will execute in the order you specify
- Common patterns:
  * Research → Analysis (for data-driven decisions)
  * Research → Creative (for informed content creation)
  * Analysis → Creative (for evaluated proposals)
  * Research → Analysis → Creative (for comprehensive projects)

Respond with ONLY the agent names in order, separated by commas. Examples:
- "research"
- "analysis"
- "research,analysis"
- "research,analysis,creative"

Query: {query}

Selected agents:"""

        try:
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=query)
            ]
            
            response = self.llm.invoke(messages)
            agent_string = response.content.strip().lower()
            
            # Parse the response
            agents = [a.strip() for a in agent_string.split(',')]
            
            # Validate agents
            valid_agents = [a for a in agents if a in self.agents_info]
            
            if not valid_agents:
                logger.warning(f"LLM returned invalid agents: {agent_string}, defaulting to research")
                return ["research"]
            
            return valid_agents
            
        except Exception as e:
            logger.error(f"LLM selection failed: {e}, falling back to keyword selection")
            return self._keyword_based_selection(query)
    
    def explain_selection(self, agents: List[str]) -> str:
        """Generate explanation for why these agents were selected"""
        if len(agents) == 1:
            agent_info = self.agents_info[agents[0]]
            return f"Using {agent_info['name']} - {agent_info['description']}"
        else:
            explanations = []
            for i, agent_key in enumerate(agents, 1):
                agent_info = self.agents_info[agent_key]
                explanations.append(f"{i}. {agent_info['name']}")
            
            return f"Using multiple agents in sequence:\n" + "\n".join(explanations)
