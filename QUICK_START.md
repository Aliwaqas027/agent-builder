# Quick Start Guide - Get Running in 10 Minutes

## Step 1: Create Dify Agents (5 minutes)

### Go to Dify Dashboard
1. Visit [https://cloud.dify.ai](https://cloud.dify.ai) or your Dify instance
2. Sign in or create an account

### Create Agent 1: Research Agent

1. Click **"Create Application"** → Select **"Chat App"**
2. **Name:** `Research Agent`
3. Click on **"Prompt"** or **"Instructions"** section
4. Paste this prompt:

```
You are a Research Agent specialized in finding and gathering information.

Your capabilities:
- Comprehensive research on any topic
- Data collection and fact-checking
- Information synthesis and summaries
- Market research and trends

When responding:
1. Provide accurate, well-researched information
2. Present data in a clear, organized manner
3. Highlight key findings
4. Be thorough and objective

Always be evidence-based in your research.
```

5. **Save** the agent
6. Go to **"API Access"** or **Settings**
7. **Copy the App ID** (looks like: `app-xxxxxxxxxxxxx`)
8. Keep this ID - you'll need it!

### Create Agent 2: Analysis Agent

1. Create another **Chat App**
2. **Name:** `Analysis Agent`
3. Paste this prompt:

```
You are an Analysis Agent specialized in evaluation and decision-making.

Your capabilities:
- Comparative analysis
- Pros and cons evaluation
- Impact assessment
- Risk analysis
- Strategic evaluation

When responding:
1. Provide balanced, objective analysis
2. Consider multiple perspectives
3. Identify key factors and trade-offs
4. Provide actionable insights

Structure your analysis with:
- Summary
- Analysis
- Key Findings
- Recommendations

Always be analytical and solution-oriented.
```

4. **Save** and **copy the App ID**

### Create Agent 3: Creative Agent

1. Create another **Chat App**
2. **Name:** `Creative Agent`
3. Paste this prompt:

```
You are a Creative Agent specialized in content creation and innovation.

Your capabilities:
- Creative writing and copywriting
- Brainstorming and ideation
- Content generation
- Design concepts
- Innovation

When responding:
1. Be imaginative and original
2. Provide multiple creative options
3. Consider audience and context
4. Balance creativity with practicality

Focus on:
- Engaging content
- Fresh perspectives
- Innovative solutions

Always be creative and inspiring.
```

4. **Save** and **copy the App ID**

### Get Dify API Key

1. In Dify dashboard, click your **profile** (top right)
2. Go to **"API Keys"** or **"Settings"** → **"API Keys"**
3. Click **"Create API Key"**
4. **Copy the key** (you won't see it again!)

## Step 2: Get OpenAI API Key (2 minutes)

1. Go to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Sign in or create account
3. Click **"Create new secret key"**
4. **Copy the key**

## Step 3: Configure the System (1 minute)

Edit your `.env` file:

```bash
# Open the file
nano .env
# or
open -e .env
```

Add your keys:

```env
# OpenAI Configuration
OPENAI_API_KEY=sk-proj-your-actual-key-here

# Dify Configuration
DIFY_API_KEY=your-dify-api-key-here
DIFY_BASE_URL=https://api.dify.ai/v1

# Dify Agent IDs (paste the IDs you copied)
RESEARCH_AGENT_ID=app-xxxxxxxxxxxxx
ANALYSIS_AGENT_ID=app-xxxxxxxxxxxxx
CREATIVE_AGENT_ID=app-xxxxxxxxxxxxx

# Application Configuration
LOG_LEVEL=INFO
FLASK_PORT=5000
```

**Save the file** (Ctrl+O, Enter, Ctrl+X in nano)

## Step 4: Test the System (2 minutes)

### Test with CLI:

```bash
python3 main.py
```

Try these queries:
- `"What are the latest AI trends?"` → Should use Research Agent
- `"Compare cloud vs on-premise solutions"` → Should use Analysis Agent
- `"Write a tagline for a tech startup"` → Should use Creative Agent

### Or Test with Web Interface:

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

## ✅ Verification Checklist

- [ ] Created 3 agents in Dify (Research, Analysis, Creative)
- [ ] Copied all 3 App IDs
- [ ] Got Dify API Key
- [ ] Got OpenAI API Key
- [ ] Updated .env file with all keys and IDs
- [ ] Tested with `python3 main.py`
- [ ] System shows which agent is used for each query

## 🎯 Example Test Queries

**Single Agent:**
```
"What is quantum computing?"
→ Should use: Research Agent
```

**Multiple Agents:**
```
"Research AI in healthcare, analyze its benefits, and create a proposal"
→ Should use: Research Agent → Analysis Agent → Creative Agent
```

## 🔧 Troubleshooting

### "Agent not available" error
- Check that Agent IDs are correct in `.env`
- Verify agents are published in Dify dashboard
- Make sure Dify API key is valid

### "OpenAI API error"
- Verify OpenAI API key is correct
- Check you have credits in your OpenAI account

### "Module not found"
```bash
pip3 install -r requirements.txt
```

## 🎉 You're Ready!

Once configured, the system will:
1. ✅ Take your prompt
2. ✅ Intelligently select the right agent(s)
3. ✅ Execute via Dify
4. ✅ Show which agent(s) were used
5. ✅ Return the response

## 📚 Next Steps

- Try complex multi-agent queries
- Customize agent prompts in Dify for your use case
- Explore the Streamlit web interface
- Check out `test_example.py` for more examples
