import streamlit as st
from src.agents.graph import app

# ----- Page Configurations -----
st.set_page_config(page_title="Reflexive AI Agent", page_icon="🤖", layout="wide")

# ----- CSS -----
st.markdown("""
<style>
    /* Clean Dark Theme with Professional Gradients */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
        background-attachment: fixed;
    }
    
    /* Glassmorphism Card Effect */
    .main-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(148, 163, 184, 0.1);
        border-radius: 24px;
        padding: 40px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        margin: 20px auto;
        max-width: 1200px;
    }
    
    /* Modern Header */
    .modern-header {
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 50%, #d946ef 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.5rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 10px;
        letter-spacing: -0.02em;
    }
    
    .subtitle-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(59, 130, 246, 0.15);
        border: 1px solid rgba(59, 130, 246, 0.3);
        padding: 8px 20px;
        border-radius: 50px;
        color: #60a5fa;
        font-size: 0.9rem;
        font-weight: 500;
        margin: 15px auto;
        backdrop-filter: blur(10px);
    }
    
    /* Chat Messages */
    .chat-message {
        padding: 16px 20px;
        margin: 12px 0;
        border-radius: 18px;
        max-width: 85%;
        animation: slideIn 0.3s ease-out;
        position: relative;
        line-height: 1.6;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .user-chat {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        margin-left: auto;
        border-bottom-right-radius: 4px;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    }
    
    .assistant-chat {
        background: rgba(51, 65, 85, 0.8);
        color: #e2e8f0;
        margin-right: auto;
        border-bottom-left-radius: 4px;
        border: 1px solid rgba(148, 163, 184, 0.2);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    .message-label {
        font-size: 0.75rem;
        font-weight: 600;
        margin-bottom: 6px;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
        border-right: 1px solid rgba(148, 163, 184, 0.1);
    }
    
    .sidebar-header {
        color: #f8fafc;
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 2px solid rgba(59, 130, 246, 0.3);
    }
    
    .status-indicator {
        display: flex;
        align-items: center;
        gap: 10px;
        background: rgba(34, 197, 94, 0.15);
        border: 1px solid rgba(34, 197, 94, 0.3);
        padding: 12px 16px;
        border-radius: 12px;
        color: #4ade80;
        margin: 15px 0;
        font-weight: 500;
    }
    
    .status-dot {
        width: 8px;
        height: 8px;
        background: #22c55e;
        border-radius: 50%;
        animation: pulse-dot 2s infinite;
    }
    
    @keyframes pulse-dot {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    /* Button */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.5);
    }
    
    /* Chat Input Container */
    .chat-input-container {
        background: rgba(30, 41, 59, 0.8);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(148, 163, 184, 0.2);
        border-radius: 20px;
        padding: 8px;
        margin: 20px 0;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
    }
    
    /* Step Indicators */
    .step-card {
        background: rgba(59, 130, 246, 0.1);
        border-left: 4px solid #3b82f6;
        padding: 12px 18px;
        margin: 8px 0;
        border-radius: 8px;
        color: #93c5fd;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 10px;
        transition: all 0.3s ease;
        animation: fadeIn 0.4s ease-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateX(-10px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .step-card:hover {
        background: rgba(59, 130, 246, 0.2);
        transform: translateX(5px);
    }
    
    /* Metrics Cards */
    .metric-card {
        background: rgba(59, 130, 246, 0.1);
        border: 1px solid rgba(59, 130, 246, 0.2);
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        margin: 10px 0;
    }
    
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #60a5fa;
        margin-bottom: 5px;
    }
    
    .metric-label {
        font-size: 0.85rem;
        color: #94a3b8;
        font-weight: 500;
    }
    
    /* Footer */
    .modern-footer {
        text-align: center;
        padding: 30px;
        color: #64748b;
        font-size: 0.9rem;
        border-top: 1px solid rgba(148, 163, 184, 0.1);
        margin-top: 40px;
    }
    
    .powered-by {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        margin-bottom: 10px;
        color: #94a3b8;
    }
    
    .tech-badge {
        display: inline-block;
        background: rgba(59, 130, 246, 0.15);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        color: #60a5fa;
        margin: 0 4px;
        font-weight: 500;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0f172a;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #3b82f6;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #2563eb;
    }
</style>
""", unsafe_allow_html=True)

# ----- Header Section -----
st.markdown("""
<div class="main-card">
    <div style="text-align: center;">
        <h1 class="modern-header">🤖 Reflexive AI Agent</h1>
        <div class="subtitle-badge">
            <span style="width: 6px; height: 6px; background: #60a5fa; border-radius: 50%; display: inline-block;"></span>
            RAG + Reflection Pattern • Web Fallback • HR Management
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Initialize Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# ----- Sidebar -----
with st.sidebar:
    st.markdown('<div class="sidebar-header">⚙️ System Control</div>', unsafe_allow_html=True)
    
    # System Status
    st.markdown("""
    <div class="status-indicator">
        <div class="status-dot"></div>
        <div>
            <div style="font-weight: 600;">System Online</div>
            <div style="font-size: 0.8rem; opacity: 0.9;">All services operational</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔌 Active Connections")
    st.markdown("""
    <div style="color: #94a3b8; font-size: 0.9rem; line-height: 2;">
        ✓ Qdrant Cloud<br>
        ✓ Groq (Llama 3.1)<br>
        ✓ Tavily Search Agent
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Metrics
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{len(st.session_state.messages)}</div>
            <div class="metric-label">Messages</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">Active</div>
            <div class="metric-label">Session</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Clear button
    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    # Tips
    with st.expander("💡 Usage Tips"):
        st.markdown("""
        - **Be specific** for better results
        - **Ask follow-up questions** to refine
        - **Agent auto-searches** web if needed
        - **HR policies, recruitment, compliance** supported
        """)

# ----- Main Chat Area -----
st.markdown('<div class="main-card">', unsafe_allow_html=True)

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"""
        <div class="chat-message user-chat">
            <div class="message-label">You</div>
            {message["content"]}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-message assistant-chat">
            <div class="message-label">AI Agent</div>
            {message["content"]}
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ----- Chat Input Section -----
st.markdown('<div class="chat-input-container">', unsafe_allow_html=True)
if prompt := st.chat_input("Ask about HR policies, recruitment, compliance, or anything else..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# ----- Process Agent Response (if new message) -----
if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    with st.chat_message("assistant"):
        with st.status("🧠 Processing your query...", expanded=True) as status:
            final_generation = None
            inputs = {
                "input": st.session_state.messages[-1]["content"],
                "iteration_count": 0,
                "documents": []
            }

            for output in app.stream(inputs):
                for key, value in output.items():

                    if key == "guardrail":
                        if not value.get("is_allowed", True):
                            st.warning("⚠️ This query is outside my expertise (HR, Finance, & Management).")
                            final_generation = "I am sorry, but I am only authorized to answer questions regarding Human Resources, Finance, and Management."

                    elif key == "retrieve":
                        st.markdown('<div class="step-card">🔍 Searching Cloud database...</div>', unsafe_allow_html=True)
                    elif key == "grader":
                        st.markdown('<div class="step-card">⚖️ Check document relevance...</div>', unsafe_allow_html=True)
                    elif key == "refine_query":
                        st.markdown('<div class="step-card">🔧 Refining query for web search...</div>', unsafe_allow_html=True)
                    elif key == "tavily_tool":
                        st.markdown('<div class="step-card">🌐 Fetching data from Web Search...</div>', unsafe_allow_html=True)
                    elif key == "generate":
                        st.markdown('<div class="step-card">✍️ Generating final response...</div>', unsafe_allow_html=True)
                        final_generation = value["generation"]
            
            status.update(label="✅ Response generated!", state="complete", expanded=False)

        if final_generation:
            st.session_state.messages.append({"role": "assistant", "content": final_generation})
            st.rerun()
        else:
            st.error("❌ Unable to generate response. Please try again.")

# ----- Footer -----
st.markdown("""
<div class="modern-footer">
    <div class="powered-by">
        <span>✨ Powered by</span>
        <span class="tech-badge">LangGraph</span>
        <span class="tech-badge">Qdrant</span>
        <span class="tech-badge">Groq</span>
        <span class="tech-badge">Tavily</span>
    </div>
    <div>Reflexive Agent for Intelligent HR Assistance</div>
</div>
""", unsafe_allow_html=True)