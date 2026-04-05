# 🤖 Reflection Agent (HR & Finance Specialist)

A production-grade **Corrective RAG (CRAG)** system built with **LangGraph**, **Groq (Llama 3.1)**, and **Qdrant Cloud**. This agent doesn't just retrieve data; it critiques its own knowledge and performs autonomous web searches when stored data is insufficient.

![Tests](https://github.com/Lakshitha6/Reflection-Agent/actions/workflows/python-tests.yml/badge.svg)

## 🌟 Key Features

- **Self-Correction Loop**: Uses a 5-node reflection pattern to grade retrieved documents and decide if a fallback search is required.
- **Domain Guardrails**: Strict gateway node ensuring the agent only discusses Human Resources, Management, and Finance.
- **Hybrid Retrieval**: Integrates **Qdrant Cloud** (Vector DB) with **Tavily Search API** for real-time web intelligence.
- **Agentic Workflow**: Managed by LangGraph for state persistence and complex conditional edge logic.
- **Production Testing**: Comprehensive test suite using `pytest` and automated **GitHub Actions** for CI/CD.

---

## 🏗️ System Architecture

The agent follows a sophisticated "Reflect and Revise" architecture:

1. **Guardrail**: Filters out non-HR/Finance queries to save costs and maintain focus.
2. **Retrieve**: Queries local Qdrant Cloud using HuggingFace embeddings.
3. **Grade**: An LLM-based "Judge" evaluates if the retrieved context is relevant.
4. **Refine & Search**: If grading fails, the agent optimizes the query and hits the Tavily Search API.
5. **Generate**: Synthesizes a professional response using the best available data.

---

## 🚀 Tech Stack

- **Orchestration**: [LangGraph](https://github.com/langchain-ai/langgraph)
- **LLM**: [Groq](https://groq.com/) (Llama-3.1-8b-instant)
- **Vector Store**: [Qdrant Cloud](https://qdrant.tech/)
- **Embeddings**: HuggingFace (sentence-transformers/all-mpnet-base-v2)
- **Search Tool**: [Tavily AI](https://tavily.com/)
- **UI**: Streamlit
- **Testing**: Pytest & GitHub Actions

---

## 🛠️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Lakshitha6/Reflection-Agent.git
   cd Reflection-Agent
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_key_here
   TAVILY_API_KEY=your_key_here
   QDRANT_URL=your_qdrant_url
   QDRANT_API_KEY=your_qdrant_api_key
   ```

---

## 🧪 Testing

This project uses pytest for unit and integration testing.

```bash
# Run all tests
python -m pytest
```

---

## 🖥️ Usage

To launch the interactive Streamlit dashboard:

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
├── .github/
│   └── workflows/       # CI/CD Pipeline
├── src/
│   ├── agents/          # LangGraph Agentic Workflow
│   │   ├── graph.py     # LangGraph state machine
│   │   ├── nodes.py     # Agent node definitions
│   │   ├── prompts.py   # LLM prompt templates
│   │   └── state.py     # Agent state schema
│   ├── core/            # Core Utilities
│   │   ├── config_loader.py    # Configuration management
│   │   ├── data_loader.py      # Data loading utilities
│   │   └── text_splitter.py    # Text chunking logic
│   └── services/        # External Service Integrations
│       ├── search_tool.py      # Tavily Search API
│       ├── embeddings/         # Embedding Services
│       │   ├── embedding_base.py       # Base embedding class
│       │   ├── embedding_factory.py    # Factory pattern
│       │   └── embedding_provider.py   # Provider implementations
│       ├── llm/                # LLM Services
│       │   ├── llm_base.py             # Base LLM class
│       │   ├── llm_factory.py          # Factory pattern
│       │   └── llm_providers.py        # LLM provider implementations
│       └── vectorstore/        # Vector Database Services
│           ├── vector_base.py          # Base vector store class
│           ├── vector_factory.py       # Factory pattern
│           └── vector_provider.py      # Vector provider implementations
├── tests/               # Test Suite
│   ├── conftest.py      # Pytest configuration
│   ├── test_graph.py    # Graph tests
│   └── test_nodes.py    # Node tests
├── config/
│   └── settings.yaml    # YAML configuration
├── data/
│   └── raw/             # Raw data files
├── app.py               # Streamlit UI entry point
├── main.py              # Python script entry point
├── README.md            # Project documentation
└── pyproject.toml       # Project dependencies
```

---

Built with ❤️ for learning and production.
⭐ Star this repo if you find it helpful!