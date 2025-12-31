#!/usr/bin/env python3
"""
Helper script to configure the system with a new Dify Chat App
"""

print("\n" + "="*70)
print("  Setup Dify Chat App")
print("="*70 + "\n")

print("""
Since Agent apps are complex, let's create a simple Chat App instead.

Follow these steps in Dify:

1. Go to: https://cloud.dify.ai
2. Click "Create Application" or "+ New App"
3. Select "Chatbot" or "Chat App" (NOT Agent!)
4. Configure:
   - Name: Research Agent
   - Model: OpenAI / gpt-4o-mini
   - System Prompt: "You are a helpful research assistant"
5. Click "Publish"
6. Copy the App ID from the URL or API Access section

The App ID looks like: app-xxxxxxxxxxxxx
""")

print("-" * 70)
print("\nOnce you have created the Chat App, enter the details:\n")

app_id = input("Paste your new Chat App ID: ").strip()

if not app_id:
    print("\n❌ App ID is required!")
    exit(1)

if not app_id.startswith('app-'):
    print(f"\n⚠️  Warning: App ID should start with 'app-'")
    print(f"You entered: {app_id}")
    confirm = input("Continue anyway? (yes/no): ").strip().lower()
    if confirm not in ['yes', 'y']:
        exit(1)

# Read current .env
try:
    with open('.env', 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    print("❌ .env file not found!")
    exit(1)

# Update agent IDs
new_lines = []
for line in lines:
    if line.startswith('RESEARCH_AGENT_ID='):
        new_lines.append(f'RESEARCH_AGENT_ID={app_id}\n')
    elif line.startswith('ANALYSIS_AGENT_ID='):
        new_lines.append(f'ANALYSIS_AGENT_ID={app_id}\n')
    elif line.startswith('CREATIVE_AGENT_ID='):
        new_lines.append(f'CREATIVE_AGENT_ID={app_id}\n')
    else:
        new_lines.append(line)

# Save
with open('.env', 'w') as f:
    f.writelines(new_lines)

print("\n" + "="*70)
print("✅ Configuration Updated!")
print("="*70 + "\n")

print(f"All agents now use: {app_id}")
print("\nTesting the configuration...\n")

# Test the API
import requests
import json

api_key = app_id
url = "https://api.dify.ai/v1/chat-messages"

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

payload = {
    "inputs": {},
    "query": "Hello",
    "response_mode": "streaming",
    "user": "test"
}

try:
    response = requests.post(url, headers=headers, json=payload, stream=True, timeout=10)
    
    if response.status_code == 200:
        print("✅ SUCCESS! The Chat App is working!")
        print("\nYou can now run:")
        print("  python3 main.py")
        print("\nOr try the web interface:")
        print("  streamlit run app.py")
    else:
        print(f"❌ Error {response.status_code}")
        print(f"Response: {response.text[:500]}")
        print("\nMake sure:")
        print("  1. The Chat App is published in Dify")
        print("  2. The model (gpt-4o-mini) is configured")
        print("  3. The App ID is correct")
        
except Exception as e:
    print(f"❌ Connection error: {e}")
    print("\nThe App ID has been saved to .env")
    print("Try running: python3 main.py")

print("\n" + "="*70 + "\n")
