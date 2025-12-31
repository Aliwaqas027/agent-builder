from .base_agent import BaseDifyAgent
from config import config


class ResearchAgent(BaseDifyAgent):
    """
    Research Agent - Handles research, data gathering, and information retrieval
    
    Specializes in:
    - Finding information
    - Data collection
    - Fact-checking
    - Literature reviews
    - Market research
    """
    
    def __init__(self):
        super().__init__(
            agent_id=config.research_agent.agent_id,
            agent_name=config.research_agent.name,
            dify_api_key=config.dify_api_key,
            dify_base_url=config.dify_base_url
        )
        self.keywords = config.research_agent.keywords
        self.description = config.research_agent.description
