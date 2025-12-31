from .base_agent import BaseDifyAgent
from config import config


class AnalysisAgent(BaseDifyAgent):
    """
    Analysis Agent - Performs analysis, evaluation, and decision-making tasks
    
    Specializes in:
    - Comparative analysis
    - Pros and cons evaluation
    - Impact assessment
    - Risk analysis
    - Strategic evaluation
    """
    
    def __init__(self):
        super().__init__(
            agent_id=config.analysis_agent.agent_id,
            agent_name=config.analysis_agent.name,
            dify_api_key=config.dify_api_key,
            dify_base_url=config.dify_base_url
        )
        self.keywords = config.analysis_agent.keywords
        self.description = config.analysis_agent.description
