# Setup Guide - Dify-LangGraph Agent System

## 📋 Prerequisites

1. **Python 3.9 or higher**
2. **Dify Account** - Sign up at [dify.ai](https://dify.ai)
3. **OpenAI API Key** - Get from [platform.openai.com](https://platform.openai.com)

## 🚀 Step-by-Step Setup

### Step 1: Create Dify Agents

You need to create 3 agents in Dify. Here's how:

#### 1.1 Research Agent

1. Log into your Dify dashboard
2. Click "Create Application" → "Chat App"
3. Name it: **Research Agent**
4. Configure the agent with this prompt:

```
You are a Research Agent specialized in finding, gathering, and presenting information.

Your capabilities:
- Comprehensive research on any topic
- Data collection and fact-checking
- Literature reviews and summaries
- Market research and trends analysis
- Information synthesis

When responding:
1. Provide accurate, well-researched information
2. Cite sources when possible
3. Present data in a clear, organized manner
4. Highlight key findings
5. Suggest related areas for further research

Always be thorough, objective, and evidence-based in your research.
```

5. Save and note the **App ID** from the URL or settings

#### 1.2 Analysis Agent

1. Create another Chat App
2. Name it: **Analysis Agent**
3. Configure with this prompt:

```
You are an Analysis Agent specialized in evaluation, comparison, and decision-making.

Your capabilities:
- Comparative analysis
- Pros and cons evaluation
- Impact assessment
- Risk analysis
- Strategic evaluation
- SWOT analysis

When responding:
1. Provide balanced, objective analysis
2. Consider multiple perspectives
3. Identify key factors and trade-offs
4. Highlight risks and opportunities
5. Provide actionable insights

Structure your analysis clearly with:
- Executive Summary
- Detailed Analysis
- Key Findings
- Recommendations

Always be analytical, critical, and solution-oriented.
```

4. Save and note the **App ID**

#### 1.3 Creative Agent

1. Create another Chat App
2. Name it: **Creative Agent**
3. Configure with this prompt:

```
You are a Creative Agent specialized in content creation and innovation.

Your capabilities:
- Creative writing and copywriting
- Brainstorming and ideation
- Content generation
- Design concepts
- Innovation and problem-solving

When responding:
1. Be imaginative and original
2. Provide multiple creative options when appropriate
3. Consider audience and context
4. Balance creativity with practicality
5. Explain your creative choices

Focus on:
- Engaging and compelling content
- Fresh perspectives
- Innovative solutions
- Clear communication

Always be creative, inspiring, and audience-focused.
```

4. Save and note the **App ID**

### Step 2: Get API Keys

#### 2.1 Dify API Key

1. In Dify dashboard, go to your profile settings
2. Navigate to "API Keys" section
3. Click "Create API Key"
4. Copy the key (you won't see it again!)

#### 2.2 OpenAI API Key

1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign in or create an account
3. Navigate to API Keys section
4. Create a new secret key
5. Copy the key

### Step 3: Install the Project

```bash
# Clone or navigate to the project directory
cd windsurf-project-2

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 4: Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env file
nano .env  # or use your preferred editor
```

Add your keys and agent IDs:

```env
# OpenAI Configuration
OPENAI_API_KEY=sk-your-openai-key-here

# Dify Configuration
DIFY_API_KEY=your-dify-api-key-here
DIFY_BASE_URL=https://api.dify.ai/v1

# Dify Agent IDs (from Step 1)
RESEARCH_AGENT_ID=your-research-agent-id-here
ANALYSIS_AGENT_ID=your-analysis-agent-id-here
CREATIVE_AGENT_ID=your-creative-agent-id-here

# Application Configuration
LOG_LEVEL=INFO
FLASK_PORT=5000
```

### Step 5: Test the Installation

```bash
# Run the test example
python test_example.py
```

This will run through several example queries to verify everything is working.

## 🎮 Usage Options

### Option 1: Command Line Interface

```bash
# Interactive mode
python main.py

# Single query mode
python main.py "What are the latest AI trends?"
```

### Option 2: Web Interface

```bash
# Start the Streamlit app
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

### Option 3: Python API

```python
from agent_system import DifyLangGraphSystem

system = DifyLangGraphSystem()
result = system.process_query("Your question here")

print(f"Response: {result['response']}")
print(f"Agents Used: {result['agents_used_display']}")
```

## 🔧 Troubleshooting

### Issue: "Agent not available"

**Solution:** Check that:
- Agent IDs are correctly set in `.env`
- Dify API key is valid
- Agents are published in Dify dashboard

### Issue: "OpenAI API error"

**Solution:** Verify:
- OpenAI API key is correct
- You have credits in your OpenAI account
- API key has proper permissions

### Issue: "Module not found"

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: Slow responses

**Solution:**
- Dify agents may take time to process
- Check your internet connection
- Verify Dify service status

## 📊 Verifying Agent Selection

The system should automatically select:

- **Research Agent** for queries like:
  - "What are the latest trends in..."
  - "Find information about..."
  - "Research the topic of..."

- **Analysis Agent** for queries like:
  - "Compare X and Y"
  - "What are the pros and cons of..."
  - "Analyze the impact of..."

- **Creative Agent** for queries like:
  - "Write a tagline for..."
  - "Brainstorm ideas for..."
  - "Create a proposal for..."

- **Multiple Agents** for complex queries like:
  - "Research X, analyze its potential, and create a proposal"

## 🎯 Next Steps

1. Try the example queries in the web interface
2. Experiment with different types of questions
3. Monitor which agents are selected for different queries
4. Customize agent prompts in Dify for your specific use case

## 📚 Additional Resources

- [Dify Documentation](https://docs.dify.ai)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## 🤝 Support

If you encounter issues:
1. Check the logs for detailed error messages
2. Verify all configuration in `.env`
3. Test each agent individually in Dify dashboard
4. Ensure all API keys are valid and have proper permissions
