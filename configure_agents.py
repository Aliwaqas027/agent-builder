#!/usr/bin/env python3
"""
Quick configuration script to update Dify agent credentials
"""
import os


def main():
    print("\n" + "="*70)
    print("  Dify Agent Configuration")
    print("="*70 + "\n")
    
    print("Great! You've created the agents in Dify.")
    print("Now let's configure the system to use them.\n")
    
    # Get Dify API Key
    print("STEP 1: Dify API Key")
    print("-" * 70)
    print("In your Dify dashboard:")
    print("1. Click your profile (top right)")
    print("2. Go to 'API Keys' or 'Settings' → 'API Keys'")
    print("3. Copy your API key\n")
    
    dify_key = input("Paste your Dify API Key: ").strip()
    
    # Get Agent IDs
    print("\n\nSTEP 2: Agent IDs")
    print("-" * 70)
    print("For each agent in Dify:")
    print("1. Open the agent")
    print("2. Look at the URL or go to Settings/API")
    print("3. Copy the App ID (looks like: app-xxxxxxxxxxxxx)\n")
    
    research_id = input("Research Agent ID: ").strip()
    analysis_id = input("Analysis Agent ID: ").strip()
    creative_id = input("Creative Agent ID: ").strip()
    
    # Get OpenAI Key
    print("\n\nSTEP 3: OpenAI API Key")
    print("-" * 70)
    print("Get from: https://platform.openai.com/api-keys\n")
    
    openai_key = input("OpenAI API Key: ").strip()
    
    # Dify Base URL
    print("\n\nSTEP 4: Dify Base URL")
    print("-" * 70)
    print("Press Enter for default (https://api.dify.ai/v1)")
    print("Or enter your custom Dify URL if self-hosting\n")
    
    dify_url = input("Dify Base URL (press Enter for default): ").strip()
    if not dify_url:
        dify_url = "https://api.dify.ai/v1"
    
    # Create .env content
    env_content = f"""# OpenAI Configuration
OPENAI_API_KEY={openai_key}

# Dify Configuration
DIFY_API_KEY={dify_key}
DIFY_BASE_URL={dify_url}

# Dify Agent IDs
RESEARCH_AGENT_ID={research_id}
ANALYSIS_AGENT_ID={analysis_id}
CREATIVE_AGENT_ID={creative_id}

# Application Configuration
LOG_LEVEL=INFO
FLASK_PORT=5000
"""
    
    # Save to .env
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        
        print("\n" + "="*70)
        print("✅ Configuration saved successfully!")
        print("="*70 + "\n")
        
        print("Your configuration:")
        print(f"  Dify API Key: {'*' * 30}{dify_key[-4:] if len(dify_key) > 4 else '****'}")
        print(f"  Dify URL: {dify_url}")
        print(f"  Research Agent: {research_id}")
        print(f"  Analysis Agent: {analysis_id}")
        print(f"  Creative Agent: {creative_id}")
        print(f"  OpenAI Key: {'*' * 30}{openai_key[-4:] if len(openai_key) > 4 else '****'}")
        
        print("\n" + "="*70)
        print("🚀 Ready to test!")
        print("="*70 + "\n")
        print("Run: python3 main.py")
        print("\nTry these queries:")
        print('  • "What are the latest AI trends?"')
        print('  • "Compare cloud vs on-premise solutions"')
        print('  • "Write a tagline for a tech startup"')
        print('  • "Research AI in healthcare, analyze benefits, create proposal"')
        
    except Exception as e:
        print(f"\n❌ Error saving configuration: {e}")
        print("Please manually edit the .env file")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Configuration cancelled")
    except Exception as e:
        print(f"\n❌ Error: {e}")
