#!/usr/bin/env python3
"""
Interactive setup helper for Dify-LangGraph Agent System
Guides you through the configuration process
"""
import os
import sys


def print_header(text):
    """Print a formatted header"""
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70 + "\n")


def print_step(number, text):
    """Print a step number"""
    print(f"\n{'─'*70}")
    print(f"STEP {number}: {text}")
    print('─'*70 + "\n")


def get_input(prompt, required=True):
    """Get user input with validation"""
    while True:
        value = input(f"{prompt}: ").strip()
        if value or not required:
            return value
        print("❌ This field is required. Please enter a value.")


def check_env_file():
    """Check if .env file exists"""
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        print("Creating .env file from template...")
        if os.path.exists('.env.example'):
            os.system('cp .env.example .env')
            print("✅ Created .env file")
        else:
            print("❌ .env.example not found!")
            return False
    return True


def main():
    """Main setup process"""
    print_header("Dify-LangGraph Agent System - Setup Helper")
    
    print("""
This helper will guide you through setting up your agent system.

You'll need:
1. A Dify account (sign up at https://cloud.dify.ai)
2. An OpenAI API key (get from https://platform.openai.com)
3. 3 Dify agents created (Research, Analysis, Creative)

Let's get started!
    """)
    
    input("Press Enter to continue...")
    
    # Check .env file
    print_step(1, "Checking Configuration File")
    if not check_env_file():
        print("\n❌ Setup cannot continue without .env file")
        sys.exit(1)
    
    print("✅ .env file found")
    
    # Get OpenAI API Key
    print_step(2, "OpenAI API Key")
    print("""
Get your OpenAI API key:
1. Go to: https://platform.openai.com/api-keys
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key (starts with 'sk-')
    """)
    
    openai_key = get_input("Paste your OpenAI API key")
    
    # Get Dify API Key
    print_step(3, "Dify API Key")
    print("""
Get your Dify API key:
1. Go to your Dify dashboard (https://cloud.dify.ai)
2. Click your profile (top right)
3. Go to "API Keys" or "Settings" → "API Keys"
4. Click "Create API Key"
5. Copy the key
    """)
    
    dify_key = get_input("Paste your Dify API key")
    
    # Get Dify Base URL
    print_step(4, "Dify Base URL")
    print("If you're using Dify Cloud, press Enter to use default.")
    print("If you're self-hosting, enter your Dify API URL.")
    
    dify_url = get_input("Dify Base URL (default: https://api.dify.ai/v1)", required=False)
    if not dify_url:
        dify_url = "https://api.dify.ai/v1"
    
    # Get Agent IDs
    print_step(5, "Create Dify Agents")
    print("""
Now you need to create 3 agents in Dify:

AGENT 1 - RESEARCH AGENT:
1. In Dify, click "Create Application" → "Chat App"
2. Name: "Research Agent"
3. In the prompt/instructions, paste:
   
   "You are a Research Agent specialized in finding and gathering information.
   Provide accurate, well-researched information on any topic."

4. Save the agent
5. Copy the App ID (looks like: app-xxxxxxxxxxxxx)

Have you created the Research Agent?
    """)
    
    input("Press Enter when ready to enter the Research Agent ID...")
    research_id = get_input("Research Agent ID (app-xxxxx)")
    
    print("""
AGENT 2 - ANALYSIS AGENT:
1. Create another Chat App
2. Name: "Analysis Agent"
3. Prompt: 
   
   "You are an Analysis Agent specialized in evaluation and decision-making.
   Provide balanced analysis, comparisons, and strategic insights."

4. Save and copy the App ID
    """)
    
    input("Press Enter when ready to enter the Analysis Agent ID...")
    analysis_id = get_input("Analysis Agent ID (app-xxxxx)")
    
    print("""
AGENT 3 - CREATIVE AGENT:
1. Create another Chat App
2. Name: "Creative Agent"
3. Prompt:
   
   "You are a Creative Agent specialized in content creation and innovation.
   Generate creative content, ideas, and solutions."

4. Save and copy the App ID
    """)
    
    input("Press Enter when ready to enter the Creative Agent ID...")
    creative_id = get_input("Creative Agent ID (app-xxxxx)")
    
    # Write to .env file
    print_step(6, "Saving Configuration")
    
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
    
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ Configuration saved to .env file")
    except Exception as e:
        print(f"❌ Error saving configuration: {e}")
        sys.exit(1)
    
    # Test the configuration
    print_step(7, "Testing Configuration")
    print("Let's test if everything is working...")
    
    try:
        from config import config
        print("\n✅ Configuration loaded successfully!")
        print(f"   OpenAI Key: {'*' * 20}{openai_key[-4:]}")
        print(f"   Dify Key: {'*' * 20}{dify_key[-4:]}")
        print(f"   Research Agent: {research_id}")
        print(f"   Analysis Agent: {analysis_id}")
        print(f"   Creative Agent: {creative_id}")
    except Exception as e:
        print(f"❌ Error loading configuration: {e}")
        print("Please check your .env file manually")
    
    # Final instructions
    print_header("Setup Complete!")
    print("""
🎉 Your Dify-LangGraph Agent System is now configured!

Next steps:

1. TEST THE SYSTEM:
   python3 main.py
   
   Try these queries:
   - "What are the latest AI trends?" (Research Agent)
   - "Compare cloud vs on-premise" (Analysis Agent)
   - "Write a creative tagline" (Creative Agent)

2. WEB INTERFACE:
   streamlit run app.py
   
   Then open: http://localhost:8501

3. RUN EXAMPLES:
   python3 test_example.py

The system will automatically:
✅ Select the right agent(s) for each query
✅ Show which agent(s) were used
✅ Handle multi-agent workflows for complex queries

Happy building! 🚀
    """)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Setup cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
