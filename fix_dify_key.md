# Fix: Getting the Correct Dify API Key

## The Problem
You're getting a **400 Bad Request** error because the Dify API Key is incorrect.

You provided: `app-zEpyX9lzyWkM7aX1vTym2snU`
This is your **App ID**, NOT your API Key.

## What You Need

### App ID vs API Key:
- **App ID**: `app-zEpyX9lzyWkM7aX1vTym2snU` ✅ (You have this)
- **API Key**: A longer string that looks like: `app-xxxxxx.yyyyyyyyyyyyyyy` or similar ❌ (Need this)

## How to Find Your Dify API Key

### Method 1: From the Agent's API Access Page

1. **Open your agent** in Dify (the one with ID: app-zEpyX9lzyWkM7aX1vTym2snU)

2. **Click "Publish"** button (if not already published)

3. **Click "API Access"** or "Access API" button (usually top right)

4. You'll see a page with:
   ```
   API Endpoint: https://api.dify.ai/v1
   
   API Key: [Show] or [Copy]
   ↑ This is what you need!
   
   App ID: app-zEpyX9lzyWkM7aX1vTym2snU
   ```

5. **Click "Show" or "Copy"** next to "API Key"

6. The API Key will be a long string (might look like):
   - `app-xxxxxx.yyyyyyyyyyyyyyy`
   - Or just a long random string
   - It's DIFFERENT from the App ID

### Method 2: Create New API Key

If you don't see an API Key:

1. In the API Access page, look for **"Create API Key"** or **"Generate Key"** button
2. Click it
3. Copy the generated key
4. **Save it somewhere** - you might not see it again!

### Method 3: Check Documentation

Look for a section called:
- "API Keys"
- "Secret Keys"  
- "Authentication"
- "API Credentials"

## Quick Fix

Once you have the correct API Key, run:

```bash
nano .env
```

Update this line:
```env
DIFY_API_KEY=your_actual_long_api_key_here
```

NOT the App ID!

Save and test again:
```bash
python3 main.py
```

## Visual Guide

```
┌─────────────────────────────────────────────────┐
│  Research Agent                      [API] ←────┤ Click here
├─────────────────────────────────────────────────┤
│                                                 │
│  API Access                                     │
│  ────────────────────────────────────────────  │
│                                                 │
│  API Endpoint:                                  │
│  https://api.dify.ai/v1                         │
│                                                 │
│  API Key: ●●●●●●●●●●●●●●●●●  [Show] [Copy] ←──┤ Get this!
│           ↑ This is the SECRET KEY              │
│                                                 │
│  App ID: app-zEpyX9lzyWkM7aX1vTym2snU          │
│          ↑ You already have this                │
│                                                 │
└─────────────────────────────────────────────────┘
```

## Still Can't Find It?

Try these locations in Dify:
1. Agent page → "API" button (top right)
2. Agent page → "Publish" → then "API Access"
3. Agent page → Settings → "API" tab
4. Main dashboard → Your profile → "API Keys"

## Alternative: Screenshot

If you still can't find it, take a screenshot of your Dify agent page and I can point you to exactly where it is!
