import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger(__name__)


@dataclass
class AgentConfig:
    """Configuration for a Dify agent"""
    agent_id: str
    name: str
    description: str
    keywords: list[str]


@dataclass
class SystemConfig:
    """Main system configuration"""
    openai_api_key: str
    dify_api_key: str
    dify_base_url: str
    research_agent: AgentConfig
    analysis_agent: AgentConfig
    creative_agent: AgentConfig
    log_level: str = "INFO"
    flask_port: int = 5000


def load_config() -> SystemConfig:
    """Load configuration from environment variables"""
    
    openai_key = os.getenv("OPENAI_API_KEY")
    dify_key = os.getenv("DIFY_API_KEY")
    
    if not openai_key:
        raise ValueError("OPENAI_API_KEY is required")
    if not dify_key:
        raise ValueError("DIFY_API_KEY is required")
    
    research_agent = AgentConfig(
        agent_id=os.getenv("RESEARCH_AGENT_ID", ""),
        name="Research Agent",
        description="Handles research, data gathering, and information retrieval",
        keywords=["research", "find", "search", "what", "information", "data", "facts", "learn", "discover", "investigate"]
    )
    
    analysis_agent = AgentConfig(
        agent_id=os.getenv("ANALYSIS_AGENT_ID", ""),
        name="Analysis Agent",
        description="Performs analysis, evaluation, and decision-making tasks",
        keywords=["analyze", "compare", "evaluate", "assess", "pros", "cons", "advantages", "disadvantages", "impact", "implications"]
    )
    
    creative_agent = AgentConfig(
        agent_id=os.getenv("CREATIVE_AGENT_ID", ""),
        name="Creative Agent",
        description="Handles creative tasks, content generation, and brainstorming",
        keywords=["create", "write", "design", "brainstorm", "generate", "compose", "draft", "imagine", "innovate", "develop"]
    )
    
    if not research_agent.agent_id:
        logger.warning("RESEARCH_AGENT_ID not set - Research Agent will not be available")
    if not analysis_agent.agent_id:
        logger.warning("ANALYSIS_AGENT_ID not set - Analysis Agent will not be available")
    if not creative_agent.agent_id:
        logger.warning("CREATIVE_AGENT_ID not set - Creative Agent will not be available")
    
    return SystemConfig(
        openai_api_key=openai_key,
        dify_api_key=dify_key,
        dify_base_url=os.getenv("DIFY_BASE_URL", "https://api.dify.ai/v1"),
        research_agent=research_agent,
        analysis_agent=analysis_agent,
        creative_agent=creative_agent,
        log_level=os.getenv("LOG_LEVEL", "INFO"),
        flask_port=int(os.getenv("FLASK_PORT", "5000"))
    )


config = load_config()
