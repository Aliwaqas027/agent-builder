# Create Simple Chat App in Dify (5 Minutes)

## Step-by-Step Instructions

### 1. Create New Application

1. Go to Dify dashboard: https://cloud.dify.ai
2. Click **"Create Application"** or **"+ New App"**
3. You'll see options - select **"Chatbot"** or **"Chat App"**
   - ❌ Do NOT select "Agent" or "Workflow"
   - ✅ Select "Chatbot" or "Chat App"

### 2. Configure the App

You'll see a configuration screen:

**App Name**: `Research Agent`

**Model Selection**:
- Click on the model dropdown
- Select **OpenAI** as provider
- Select **gpt-4o-mini** as model

**System Prompt** (copy this):
```
You are a Research Agent specialized in finding and gathering information.

Your capabilities:
- Comprehensive research on any topic
- Data collection and fact-checking
- Information synthesis and summaries

Provide accurate, well-researched information in a clear, organized manner.
```

**Settings** (optional):
- Temperature: 0.7
- Max tokens: 2000

### 3. Test in Dify

Before publishing, test it:
1. Use the chat interface on the right
2. Type: "What is AI?"
3. Make sure it responds correctly

### 4. Publish

1. Click **"Publish"** button (top right)
2. Confirm publish
3. Wait for "Published successfully"

### 5. Get the App ID

After publishing:
1. Look at the URL in your browser
2. It will be: `https://cloud.dify.ai/app/app-XXXXXXXXXXXXX/...`
3. Copy the part that looks like: `app-XXXXXXXXXXXXX`

OR

1. Click **"API Access"** button
2. Copy the **App ID** shown there

### 6. Update Your Configuration

Run this command:
```bash
nano .env
```

Update these lines with your NEW App ID:
```env
RESEARCH_AGENT_ID=app-your-new-id-here
ANALYSIS_AGENT_ID=app-your-new-id-here
CREATIVE_AGENT_ID=app-your-new-id-here
```

(You can use the same App ID for all three for testing)

Save: `Ctrl+O`, `Enter`, `Ctrl+X`

### 7. Test the System

```bash
python3 main.py
```

Try asking: "What is LangGraph?"

It should work! ✅

## 🎯 Key Points

- Use **"Chat App"** or **"Chatbot"** type (NOT Agent)
- Select **OpenAI / gpt-4o-mini** model
- Add a system prompt
- **Publish** the app
- Copy the **App ID**
- Update your `.env` file

## 📸 What You Should See

When creating the app, you should see:
```
┌─────────────────────────────────────┐
│ Create Application                  │
├─────────────────────────────────────┤
│                                     │
│ [Chatbot]  [Agent]  [Workflow]     │
│    ↑                                │
│  Click this!                        │
│                                     │
└─────────────────────────────────────┘
```

Then in configuration:
```
┌─────────────────────────────────────┐
│ Model: [OpenAI / gpt-4o-mini ▼]    │
│                                     │
│ System Prompt:                      │
│ ┌─────────────────────────────────┐ │
│ │ You are a Research Agent...     │ │
│ └─────────────────────────────────┘ │
│                                     │
│ [Test] [Publish]                    │
└─────────────────────────────────────┘
```

This is MUCH simpler than Agent apps and will work immediately!
