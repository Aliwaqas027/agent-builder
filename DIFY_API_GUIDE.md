# How to Get Dify API Credentials

## Method 1: From Individual Apps (Most Common)

### Getting API Key and App ID:

1. **Open your Dify dashboard** (cloud.dify.ai or your instance)

2. **Click on one of your agents** (Research Agent, Analysis Agent, or Creative Agent)

3. **Look for "API Access" or "Access API" button**
   - Usually in the top right corner
   - Or in the left sidebar menu
   - Or under "Publish" section

4. **You'll see:**
   - **API Key** (also called API Secret Key)
   - **App ID** (format: `app-xxxxxxxxxxxxx`)
   - **API Endpoint** (the base URL)

5. **Copy these values** for each of your 3 agents

### Visual Guide:
```
┌─────────────────────────────────────────┐
│  Research Agent                    [API]│  ← Click here
├─────────────────────────────────────────┤
│                                         │
│  API Access                             │
│  ├─ API Endpoint: https://api.dify.ai/v1
│  ├─ API Key: app-xxxxxx...xxxxx        │  ← Copy this
│  └─ App ID: app-xxxxxxxxxxxxx          │  ← Copy this
│                                         │
└─────────────────────────────────────────┘
```

## Method 2: From App Settings

1. Open your agent/app
2. Click **"Settings"** or gear icon ⚙️
3. Look for **"API"** or **"API Access"** tab
4. Copy the API Key and App ID

## Method 3: Service API (Alternative)

If you can't find API keys in individual apps:

1. Go to Dify dashboard main page
2. Look for **"Resources"** or **"Workspace Settings"**
3. Find **"API Keys"** or **"Service API"**
4. Create a new API key if needed

## What You Need:

For this project, you need:

### From Each Agent (3 total):
- ✅ **App ID** - Unique identifier for each agent
  - Format: `app-xxxxxxxxxxxxx`
  - Each agent has its own App ID

### One Time (Shared):
- ✅ **API Key** - Authentication key
  - Format: Long string of characters
  - Can be the same for all agents
  
- ✅ **API Endpoint** - Base URL
  - Usually: `https://api.dify.ai/v1`
  - Or your self-hosted URL

## Quick Test

Once you have the credentials, test if they work:

```bash
curl -X POST 'https://api.dify.ai/v1/chat-messages' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "inputs": {},
    "query": "Hello",
    "response_mode": "blocking",
    "user": "test"
  }'
```

If you get a response (not 401 error), your API key is working!

## Common Issues:

### "I don't see API Access button"
- Make sure the app is **published** or **deployed**
- Check if you're in "Edit" mode - switch to "Overview" or "Run"
- Look for "Publish" button first

### "API Key is empty or not showing"
- Click "Create API Key" or "Generate Key" button
- Some versions auto-generate, some require manual creation

### "401 Unauthorized Error"
- API Key is incorrect or expired
- App is not published
- Wrong API endpoint URL

## Still Can't Find It?

Try these locations in order:

1. **App Overview Page** → "API Access" button (top right)
2. **App Settings** → "API" tab
3. **Left Sidebar** → "API" or "Access API" menu item
4. **Publish Section** → After publishing, API info appears
5. **Workspace Settings** → "API Keys" (for service-level keys)

## Alternative: Use Dify's Built-in Testing

If you're still having trouble:

1. You can test agents directly in Dify's interface first
2. Make sure they work there
3. Then we can help you find the API credentials

## Need Help?

Share a screenshot of your Dify interface and I can guide you to the exact location!
