# Fix OpenAI API Key Issue

## ❌ Current Error
```
Error code: 401 - {'error': {'message': 'No such organization: nedge.', 
'type': 'invalid_request_error', 'code': 'invalid_organization'}}
```

## 🔧 Solution: Generate a New OpenAI API Key

### Step 1: Go to OpenAI Platform
Visit: https://platform.openai.com/api-keys

### Step 2: Delete Old Key (Optional)
If you see the old key listed, you can revoke it.

### Step 3: Create New API Key
1. Click **"Create new secret key"**
2. Give it a name (e.g., "Dify-LangGraph")
3. **Important**: Select permissions if asked
4. Click **"Create"**
5. **Copy the key immediately** (you won't see it again!)

### Step 4: Verify the Key Format
The key should look like:
```
sk-proj-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Make sure it:
- Starts with `sk-proj-` or `sk-`
- Is a long string (around 50+ characters)
- Has no spaces or line breaks

### Step 5: Update Your Configuration

Run this command and paste the NEW key:
```bash
nano .env
```

Update this line:
```env
OPENAI_API_KEY=your_new_key_here
```

Save: `Ctrl+O`, `Enter`, `Ctrl+X`

### Step 6: Also Update in Dify

1. Go to Dify dashboard
2. Settings → Model Providers → OpenAI
3. Replace the old key with the new one
4. Save

### Step 7: Test

```bash
python3 debug_dify.py
```

Should now work!

## 💡 Alternative: Use a Different Model Provider

If you don't want to use OpenAI, you can configure Dify to use:
- **Anthropic** (Claude)
- **Azure OpenAI**
- **Local models** (Ollama, LM Studio)
- **Other providers**

Just configure the provider in Dify workspace settings and select it in your agent.

## 🎯 Quick Test

Once you have a valid OpenAI key:
1. Add it to Dify workspace (Settings → Model Providers → OpenAI)
2. Configure your agent to use OpenAI model (gpt-4o-mini)
3. Save and Publish the agent
4. Run: `python3 main.py`

The system will work!
