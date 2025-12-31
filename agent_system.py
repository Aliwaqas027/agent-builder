import logging
from typing import Dict, Any, Optional
from orchestrator import LangGraphBrain, OrchestratorResult

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


class DifyLangGraphSystem:
    """
    Main system class that combines Dify agents with LangGraph orchestration
    """
    
    def __init__(self):
        """Initialize the system with the LangGraph brain"""
        logger.info("Initializing Dify-LangGraph System...")
        self.brain = LangGraphBrain()
        logger.info("System initialized successfully")
    
    def process_query(
        self, 
        query: str, 
        context: Optional[Dict[str, Any]] = None,
        verbose: bool = True
    ) -> Dict[str, Any]:
        """
        Process a user query through the agent system
        
        Args:
            query: User's question or request
            context: Optional additional context
            verbose: Whether to print detailed information
            
        Returns:
            Dictionary with response, agents used, and metadata
        """
        if verbose:
            print(f"\n{'='*60}")
            print(f"Query: {query}")
            print(f"{'='*60}\n")
        
        # Process through the brain
        result = self.brain.process_query(query, context)
        
        if not result.success:
            if verbose:
                print(f"❌ Error: {result.error}\n")
            return {
                "response": result.response,
                "agents_used": [],
                "success": False,
                "error": result.error
            }
        
        # Format agent information
        agents_used_str = " → ".join(result.agents_used)
        
        if verbose:
            print(f"🤖 Agents Used: {agents_used_str}")
            print(f"\n{'─'*60}\n")
            print(f"Response:\n{result.response}")
            print(f"\n{'='*60}\n")
        
        return {
            "response": result.response,
            "agents_used": result.agents_used,
            "agents_used_display": agents_used_str,
            "agent_details": result.agent_details,
            "success": True
        }
    
    def get_available_agents(self) -> Dict[str, Dict[str, str]]:
        """Get information about available agents"""
        agents_info = {}
        
        for agent_key, agent in self.brain.agents.items():
            agents_info[agent_key] = {
                "name": agent.agent_name,
                "description": agent.description,
                "available": agent.is_available(),
                "keywords": ", ".join(agent.keywords[:5])  # Show first 5 keywords
            }
        
        return agents_info
    
    def print_agent_info(self):
        """Print information about all available agents"""
        print("\n" + "="*60)
        print("Available Agents")
        print("="*60 + "\n")
        
        agents_info = self.get_available_agents()
        
        for agent_key, info in agents_info.items():
            status = "✅" if info["available"] else "❌"
            print(f"{status} {info['name']}")
            print(f"   Description: {info['description']}")
            print(f"   Keywords: {info['keywords']}")
            print()
        
        print("="*60 + "\n")
