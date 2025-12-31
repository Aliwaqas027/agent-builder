#!/usr/bin/env python3
"""
Main CLI application for Dify-LangGraph Agent System
"""
import sys
from agent_system import DifyLangGraphSystem


def print_banner():
    """Print welcome banner"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║         Dify-LangGraph Multi-Agent System                    ║
║                                                              ║
║  Dify: Agent Builder | LangGraph: Orchestration Brain       ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_help():
    """Print help information"""
    help_text = """
Commands:
  - Type your question or request
  - 'agents' - Show available agents
  - 'help' - Show this help message
  - 'exit' or 'quit' - Exit the application

Examples:
  • "What are the latest trends in AI?"
  • "Compare the benefits of cloud vs on-premise solutions"
  • "Write a creative tagline for a tech startup"
  • "Research quantum computing, analyze its market potential, and create a pitch"
    """
    print(help_text)


def interactive_mode(system: DifyLangGraphSystem):
    """Run interactive CLI mode"""
    print_banner()
    print("\nWelcome! Ask me anything and I'll route your query to the best agent(s).")
    print("Type 'help' for commands or 'exit' to quit.\n")
    
    while True:
        try:
            # Get user input
            user_input = input("\n🧑 You: ").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("\n👋 Goodbye!\n")
                break
            
            elif user_input.lower() == 'help':
                print_help()
                continue
            
            elif user_input.lower() == 'agents':
                system.print_agent_info()
                continue
            
            # Process query
            result = system.process_query(user_input, verbose=True)
            
            if not result['success']:
                print(f"\n❌ Error: {result.get('error', 'Unknown error')}\n")
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!\n")
            break
        
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}\n")


def single_query_mode(system: DifyLangGraphSystem, query: str):
    """Process a single query and exit"""
    result = system.process_query(query, verbose=True)
    
    if result['success']:
        sys.exit(0)
    else:
        sys.exit(1)


def main():
    """Main entry point"""
    try:
        # Initialize system
        system = DifyLangGraphSystem()
        
        # Check if query provided as argument
        if len(sys.argv) > 1:
            query = " ".join(sys.argv[1:])
            single_query_mode(system, query)
        else:
            interactive_mode(system)
    
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!\n")
        sys.exit(0)
    
    except Exception as e:
        print(f"\n❌ Fatal error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
