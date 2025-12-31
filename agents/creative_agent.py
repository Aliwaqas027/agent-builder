from .base_agent import BaseDifyAgent
from config import config


class CreativeAgent(BaseDifyAgent):
    """
    Creative Agent - Handles creative tasks, content generation, and brainstorming
    
    Specializes in:
    - Content creation
    - Writing and copywriting
    - Brainstorming ideas
    - Design concepts
    - Innovation and ideation
    """
    
    def __init__(self):
        super().__init__(
            agent_id=config.creative_agent.agent_id,
            agent_name=config.creative_agent.name,
            dify_api_key=config.dify_api_key,
            dify_base_url=config.dify_base_url
        )
        self.keywords = config.creative_agent.keywords
        self.description = config.creative_agent.description
