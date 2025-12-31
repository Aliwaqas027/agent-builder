"""
Example script demonstrating the Dify-LangGraph Agent System
"""
from agent_system import DifyLangGraphSystem


def main():
    """Run example queries"""
    
    print("\n" + "="*70)
    print("Dify-LangGraph Agent System - Example Usage")
    print("="*70 + "\n")
    
    # Initialize system
    print("Initializing system...")
    system = DifyLangGraphSystem()
    
    # Show available agents
    system.print_agent_info()
    
    # Example queries
    examples = [
        {
            "title": "Research Query",
            "query": "What are the latest trends in artificial intelligence?",
            "expected_agent": "Research Agent"
        },
        {
            "title": "Analysis Query",
            "query": "Compare the advantages and disadvantages of cloud computing vs on-premise infrastructure",
            "expected_agent": "Analysis Agent"
        },
        {
            "title": "Creative Query",
            "query": "Write a creative tagline for a sustainable energy company",
            "expected_agent": "Creative Agent"
        },
        {
            "title": "Multi-Agent Query (Research + Analysis)",
            "query": "Research the current state of electric vehicles and analyze their market potential",
            "expected_agent": "Research Agent → Analysis Agent"
        },
        {
            "title": "Complex Multi-Agent Query",
            "query": "Research AI applications in healthcare, analyze the implementation challenges, and create a proposal for a hospital",
            "expected_agent": "Research Agent → Analysis Agent → Creative Agent"
        }
    ]
    
    # Process each example
    for i, example in enumerate(examples, 1):
        print(f"\n{'='*70}")
        print(f"Example {i}: {example['title']}")
        print(f"Expected Agent(s): {example['expected_agent']}")
        print(f"{'='*70}\n")
        
        result = system.process_query(example['query'], verbose=True)
        
        if result['success']:
            print(f"\n✅ Success! Agents matched expectation: {result['agents_used_display']}")
        else:
            print(f"\n❌ Failed: {result.get('error', 'Unknown error')}")
        
        print("\n" + "-"*70)
        input("\nPress Enter to continue to next example...")
    
    print("\n" + "="*70)
    print("All examples completed!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
