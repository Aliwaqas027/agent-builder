"""
Streamlit Web Interface for Dify-LangGraph Agent System
"""
import streamlit as st
from agent_system import DifyLangGraphSystem
import time

st.set_page_config(
    page_title="Dify-LangGraph Agent System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


def initialize_session_state():
    """Initialize session state variables"""
    if 'system' not in st.session_state:
        st.session_state.system = DifyLangGraphSystem()
    
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    if 'query_count' not in st.session_state:
        st.session_state.query_count = 0


def render_sidebar():
    """Render sidebar with agent information"""
    st.sidebar.title("🤖 Agent System")
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("Available Agents")
    
    agents_info = st.session_state.system.get_available_agents()
    
    for agent_key, info in agents_info.items():
        with st.sidebar.expander(f"{'✅' if info['available'] else '❌'} {info['name']}"):
            st.write(f"**Description:** {info['description']}")
            st.write(f"**Keywords:** {info['keywords']}")
            st.write(f"**Status:** {'Available' if info['available'] else 'Not Configured'}")
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("Statistics")
    st.sidebar.metric("Queries Processed", st.session_state.query_count)
    
    if st.sidebar.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.session_state.query_count = 0
        st.rerun()


def render_example_queries():
    """Render example query buttons"""
    st.subheader("💡 Try These Examples")
    
    col1, col2, col3 = st.columns(3)
    
    examples = [
        ("🔍 Research", "What are the latest trends in renewable energy?"),
        ("📊 Analysis", "Compare the pros and cons of remote work vs office work"),
        ("✨ Creative", "Write a creative tagline for an AI-powered healthcare startup"),
        ("🔬 Research", "Find information about quantum computing applications"),
        ("⚖️ Analysis", "Analyze the impact of AI on job markets"),
        ("🎨 Creative", "Brainstorm innovative features for a smart home app"),
        ("🔄 Multi-Agent", "Research AI in education, analyze its benefits, and create a proposal"),
        ("🌟 Complex", "Investigate blockchain technology, evaluate its risks, and design a use case"),
        ("📈 Combined", "Study market trends in EVs, assess investment potential, and draft a pitch")
    ]
    
    cols = [col1, col2, col3]
    for i, (label, query) in enumerate(examples):
        with cols[i % 3]:
            if st.button(label, key=f"example_{i}", use_container_width=True):
                return query
    
    return None


def render_chat_interface():
    """Render main chat interface"""
    st.title("🤖 Dify-LangGraph Multi-Agent System")
    st.markdown("**Dify as Agent Builder | LangGraph as Orchestration Brain**")
    st.markdown("---")
    
    # Display example queries
    example_query = render_example_queries()
    
    st.markdown("---")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
            # Show agent information for assistant messages
            if message["role"] == "assistant" and "agents_used" in message:
                agents_display = message.get("agents_used_display", "Unknown")
                
                if message.get("success", False):
                    st.success(f"🤖 **Agents Used:** {agents_display}")
                else:
                    st.error(f"❌ **Error:** {message.get('error', 'Unknown error')}")
    
    # Handle example query click
    if example_query:
        process_query(example_query)
        st.rerun()
    
    # Chat input
    if prompt := st.chat_input("Type your question or request..."):
        process_query(prompt)
        st.rerun()


def process_query(prompt: str):
    """Process a user query"""
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Process with system
    with st.chat_message("assistant"):
        with st.spinner("🧠 Analyzing query and selecting agents..."):
            result = st.session_state.system.process_query(prompt, verbose=False)
        
        # Display response
        if result['success']:
            st.markdown(result['response'])
            
            agents_display = result.get('agents_used_display', 'Unknown')
            st.success(f"🤖 **Agents Used:** {agents_display}")
            
            # Show detailed agent information
            with st.expander("📊 Agent Execution Details"):
                for detail in result.get('agent_details', []):
                    agent_name = detail.get('agent_name', 'Unknown')
                    success = detail.get('success', False)
                    
                    if success:
                        st.write(f"✅ **{agent_name}**")
                        st.write(f"Response length: {len(detail.get('content', ''))} characters")
                    else:
                        st.write(f"❌ **{agent_name}**")
                        st.write(f"Error: {detail.get('error', 'Unknown')}")
        else:
            error_msg = result.get('error', 'Unknown error occurred')
            st.error(f"❌ **Error:** {error_msg}")
            st.markdown(result['response'])
        
        # Add assistant message to history
        st.session_state.messages.append({
            "role": "assistant",
            "content": result['response'],
            "agents_used": result.get('agents_used', []),
            "agents_used_display": result.get('agents_used_display', 'Unknown'),
            "success": result['success'],
            "error": result.get('error')
        })
        
        # Increment query count
        st.session_state.query_count += 1


def main():
    """Main application"""
    initialize_session_state()
    render_sidebar()
    render_chat_interface()


if __name__ == "__main__":
    main()
