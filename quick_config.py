#!/usr/bin/env python3
"""
Quick configuration with provided credentials
"""

# Your Dify App ID
app_id = "app-zEpyX9lzyWkM7aX1vTym2snU"

print("\n" + "="*70)
print("  Quick Configuration Setup")
print("="*70 + "\n")

print(f"✅ App ID found: {app_id}\n")

print("Now I need a few more details:\n")

# Get Dify API Key
print("1. DIFY API KEY")
print("-" * 70)
print("In your Dify agent, click 'API Access' or 'Access API'")
print("Copy the API Key (long string of characters)\n")
dify_key = input("Paste your Dify API Key: ").strip()

# Ask if same agent for all or different
print("\n2. AGENT SETUP")
print("-" * 70)
print("Do you want to use the SAME agent for all 3 roles?")
print("(Research, Analysis, Creative)")
print("This is fine for testing - you can create separate agents later.\n")
same_agent = input("Use same agent for all? (yes/no): ").strip().lower()

if same_agent in ['yes', 'y']:
    research_id = app_id
    analysis_id = app_id
    creative_id = app_id
    print(f"\n✅ Using {app_id} for all agents")
else:
    print("\nEnter the App IDs for each agent:")
    research_id = input("Research Agent ID: ").strip() or app_id
    analysis_id = input("Analysis Agent ID: ").strip() or app_id
    creative_id = input("Creative Agent ID: ").strip() or app_id

# Get OpenAI Key
print("\n3. OPENAI API KEY")
print("-" * 70)
print("Get from: https://platform.openai.com/api-keys\n")
openai_key = input("Paste your OpenAI API Key: ").strip()

# Create .env file
env_content = f"""# OpenAI Configuration
OPENAI_API_KEY={openai_key}

# Dify Configuration
DIFY_API_KEY={dify_key}
DIFY_BASE_URL=https://api.dify.ai/v1

# Dify Agent IDs
RESEARCH_AGENT_ID={research_id}
ANALYSIS_AGENT_ID={analysis_id}
CREATIVE_AGENT_ID={creative_id}

# Application Configuration
LOG_LEVEL=INFO
FLASK_PORT=5000
"""

try:
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("\n" + "="*70)
    print("✅ Configuration saved successfully!")
    print("="*70 + "\n")
    
    print("Configuration:")
    print(f"  Dify API Key: {'*' * 30}{dify_key[-4:] if len(dify_key) > 4 else '****'}")
    print(f"  Research Agent: {research_id}")
    print(f"  Analysis Agent: {analysis_id}")
    print(f"  Creative Agent: {creative_id}")
    print(f"  OpenAI Key: {'*' * 30}{openai_key[-4:] if len(openai_key) > 4 else '****'}")
    
    print("\n" + "="*70)
    print("🚀 Ready to test!")
    print("="*70 + "\n")
    print("Run: python3 main.py")
    print("\nTry:")
    print('  "What are AI agents?"')
    print('  "Compare cloud vs on-premise"')
    print('  "Write a creative tagline"')
    
except Exception as e:
    print(f"\n❌ Error: {e}")

