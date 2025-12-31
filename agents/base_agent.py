import requests
import logging
import json
from typing import Dict, Any, Optional
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class AgentResponse:
    """Response from an agent"""
    content: str
    agent_name: str
    success: bool
    metadata: Dict[str, Any] = None
    error: Optional[str] = None


class BaseDifyAgent:
    """Base class for Dify-powered agents"""
    
    def __init__(self, agent_id: str, agent_name: str, dify_api_key: str, dify_base_url: str):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.dify_api_key = dify_api_key
        self.dify_base_url = dify_base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {dify_api_key}',
            'Content-Type': 'application/json'
        })
    
    def execute(
        self, 
        query: str, 
        conversation_id: Optional[str] = None,
        user_id: str = "default",
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Execute the agent with a query
        
        Args:
            query: User query
            conversation_id: Optional conversation ID for context
            user_id: User identifier
            context: Additional context
            
        Returns:
            AgentResponse with the result
        """
        try:
            logger.info(f"{self.agent_name} processing query: {query[:100]}...")
            
            url = f"{self.dify_base_url}/chat-messages"
            
            payload = {
                "inputs": context or {},
                "query": query,
                "response_mode": "streaming",
                "user": user_id
            }
            
            if conversation_id:
                payload["conversation_id"] = conversation_id
            
            response = self.session.post(url, json=payload, timeout=30, stream=True)
            response.raise_for_status()
            
            # Parse streaming response
            answer = ""
            conv_id = None
            msg_id = None
            
            for line in response.iter_lines():
                if line:
                    line_text = line.decode('utf-8')
                    if line_text.startswith('data: '):
                        try:
                            data = json.loads(line_text[6:])
                            event = data.get('event')
                            
                            if event == 'message':
                                # Accumulate answer chunks
                                answer += data.get('answer', '')
                            elif event == 'agent_message':
                                answer += data.get('answer', '')
                            elif event == 'message_end':
                                conv_id = data.get('conversation_id')
                                msg_id = data.get('id')
                        except json.JSONDecodeError:
                            continue
            
            logger.info(f"{self.agent_name} completed successfully")
            
            return AgentResponse(
                content=answer,
                agent_name=self.agent_name,
                success=True,
                metadata={
                    'conversation_id': conv_id,
                    'message_id': msg_id,
                    'agent_id': self.agent_id
                }
            )
            
        except requests.exceptions.RequestException as e:
            error_msg = str(e)
            logger.error(f"{self.agent_name} API error: {error_msg}")
            
            # Try to get more details from response
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_detail = e.response.text
                    logger.error(f"{self.agent_name} Error details: {error_detail[:500]}")
                except:
                    pass
            
            return AgentResponse(
                content="",
                agent_name=self.agent_name,
                success=False,
                error=f"API error: {error_msg}"
            )
        except Exception as e:
            logger.error(f"{self.agent_name} unexpected error: {str(e)}")
            return AgentResponse(
                content="",
                agent_name=self.agent_name,
                success=False,
                error=f"Unexpected error: {str(e)}"
            )
    
    def is_available(self) -> bool:
        """Check if the agent is properly configured"""
        return bool(self.agent_id and self.dify_api_key)
