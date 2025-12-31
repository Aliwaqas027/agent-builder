# Dify-LangGraph Agent System

A multi-agent system that uses **Dify as the agent builder** and **LangGraph as the orchestration brain**. The system intelligently selects the appropriate agent(s) based on user prompts and tracks which agents are used in the response.

## 🎯 Architecture

```
User Prompt → LangGraph Brain → Agent Selector → Dify Agents → Response
                    ↓                                    ↓
              Agent Tracking                    Agent Execution
```

## 🤖 Three Specialized Agents

1. **Research Agent** - Handles research, data gathering, and information retrieval
2. **Analysis Agent** - Performs analysis, evaluation, and decision-making tasks
3. **Creative Agent** - Handles creative tasks, content generation, and brainstorming

## 🚀 Features

- **Intelligent Agent Selection**: LangGraph brain automatically selects the best agent(s) for each query
- **Multi-Agent Collaboration**: Can use multiple agents for complex tasks
- **Agent Tracking**: Shows which agent(s) were used in the response
- **Dify Integration**: Each agent is built and managed in Dify
- **Conversation Memory**: Maintains context across interactions

## 📋 Prerequisites

- Python 3.9+
- Dify account with API access
- OpenAI API key
- 3 Dify agents created (Research, Analysis, Creative)

## 🛠️ Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys and Dify agent IDs
```

## ⚙️ Configuration

Create three agents in Dify and add their IDs to `.env`:

```env
OPENAI_API_KEY=your_openai_key
DIFY_API_KEY=your_dify_key
DIFY_BASE_URL=https://api.dify.ai/v1

# Agent IDs from Dify
RESEARCH_AGENT_ID=your_research_agent_id
ANALYSIS_AGENT_ID=your_analysis_agent_id
CREATIVE_AGENT_ID=your_creative_agent_id
```

## 🎮 Usage

### Command Line Interface

```bash
python main.py
```

### Python API

```python
from agent_system import DifyLangGraphSystem

system = DifyLangGraphSystem()
result = system.process_query("Analyze the impact of AI on healthcare")

print(f"Response: {result['response']}")
print(f"Agents Used: {result['agents_used']}")
```

### Web Interface

```bash
streamlit run app.py
```

## 📖 Example Interactions

**Research Query:**
```
User: "What are the latest trends in renewable energy?"
Agent Used: Research Agent
Response: [Detailed research findings...]
```

**Analysis Query:**
```
User: "Compare the pros and cons of solar vs wind energy"
Agents Used: Research Agent → Analysis Agent
Response: [Comprehensive analysis...]
```

**Creative Query:**
```
User: "Write a tagline for a sustainable energy company"
Agent Used: Creative Agent
Response: [Creative tagline...]
```

**Complex Query:**
```
User: "Research AI trends, analyze market potential, and create a pitch"
Agents Used: Research Agent → Analysis Agent → Creative Agent
Response: [Multi-agent collaborative response...]
```

## 🏗️ Project Structure

```
windsurf-project-2/
├── main.py                 # CLI entry point
├── app.py                  # Streamlit web interface
├── agent_system.py         # Core agent system
├── agents/
│   ├── base_agent.py      # Base agent class
│   ├── research_agent.py  # Research agent
│   ├── analysis_agent.py  # Analysis agent
│   └── creative_agent.py  # Creative agent
├── orchestrator/
│   ├── brain.py           # LangGraph orchestrator
│   └── selector.py        # Agent selection logic
├── config.py              # Configuration management
├── requirements.txt       # Dependencies
└── .env.example          # Environment template
```

## 🧠 How It Works

1. **User Input**: User provides a prompt
2. **LangGraph Brain**: Analyzes the prompt and determines required capabilities
3. **Agent Selection**: Selects one or more agents based on task requirements
4. **Dify Execution**: Selected agents process the task via Dify API
5. **Response Aggregation**: Combines responses if multiple agents are used
6. **Agent Tracking**: Returns response with agent usage information

## 🔧 Advanced Features

- **Sequential Processing**: Agents can work in sequence for complex tasks
- **Parallel Processing**: Multiple agents can work simultaneously
- **Context Preservation**: Maintains conversation history
- **Error Handling**: Graceful fallbacks if agents fail
- **Performance Metrics**: Tracks response times and agent efficiency

## 📊 Agent Selection Logic

The LangGraph brain uses keyword analysis and intent classification:

- **Research Keywords**: "research", "find", "what", "information", "data"
- **Analysis Keywords**: "analyze", "compare", "evaluate", "assess", "pros and cons"
- **Creative Keywords**: "create", "write", "design", "brainstorm", "generate"

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License
