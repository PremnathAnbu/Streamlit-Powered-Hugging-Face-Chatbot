---
title: Streamlit Powered Hugging Face Chatbot
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: streamlit
sdk_version: "1.45.1"
python_version: "3.11"
app_file: app.py
pinned: false
---

# 🤖 Streamlit Powered Hugging Face Chatbot

An end-to-end AI chatbot application built using Streamlit, Hugging Face, LangChain, and LangGraph.

## 🚀 Features

- Interactive chatbot UI
- Multi-LLM support
- Streamlit frontend
- Agentic AI workflow
- Hugging Face deployment ready

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```




# 🤖 Streamlit Powered Hugging Face Chatbot

An end-to-end agentic AI chatbot application built with **Streamlit**, **Hugging Face**, **LangChain**, and **LangGraph**. This project demonstrates how to build a production-ready, multi-LLM chatbot with an agentic workflow, deployable directly to Hugging Face Spaces.

---

## 🚀 Features

- **Interactive Chat UI** — Clean, responsive chatbot interface powered by Streamlit
- **Multi-LLM Support** — Easily swap between different language models (via Groq and Hugging Face Hub)
- **Agentic AI Workflow** — Built on LangGraph for stateful, graph-based agent orchestration
- **Web Search Tool** — Integrated Tavily search for real-time information retrieval
- **Vector Store** — FAISS-based document retrieval for RAG-style capabilities
- **Hugging Face Spaces Ready** — Configured for seamless one-click deployment

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| LLM Orchestration | LangChain, LangGraph |
| LLM Providers | Groq, Hugging Face Hub |
| Search Tool | Tavily Python |
| Vector Store | FAISS |
| Language | Python 3.11 |

---

## 📁 Project Structure

```
Streamlit-Powered-Hugging-Face-Chatbot/
├── app.py                          # Application entry point
├── requirements.txt                # Python dependencies
├── setup.sh                        # Project scaffold script
├── .gitignore
└── src/
    └── langgraphagenticai/
        ├── main.py                 # Loads and launches the app
        ├── graph/                  # LangGraph workflow definitions
        ├── LLMS/                   # LLM provider configurations
        ├── nodes/                  # Graph node logic
        ├── state/                  # Agent state management
        ├── tools/                  # Tool definitions (e.g., Tavily search)
        ├── vectorstore/            # FAISS vector store setup
        └── ui/
            └── streamlitui/        # Streamlit UI components & config
```

---

## ⚙️ Prerequisites

- Python 3.11+
- A [Groq API key](https://console.groq.com/) or [Hugging Face token](https://huggingface.co/settings/tokens)
- A [Tavily API key](https://tavily.com/) (for web search functionality)

---

## 🏃 Run Locally

**1. Clone the repository**

```bash
git clone https://github.com/PremnathAnbu/Streamlit-Powered-Hugging-Face-Chatbot.git
cd Streamlit-Powered-Hugging-Face-Chatbot
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Set up environment variables**

Create a `.env` file or export your keys in the terminal:

```bash
export GROQ_API_KEY=your_groq_api_key
export HUGGINGFACEHUB_API_TOKEN=your_hf_token
export TAVILY_API_KEY=your_tavily_api_key
```

**4. Run the app**

```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`.

---

## ☁️ Deploy to Hugging Face Spaces

This project is pre-configured for Hugging Face Spaces deployment.

1. Fork or push this repository to your Hugging Face account.
2. Create a new **Space** with the **Streamlit** SDK.
3. Add your API keys as **Secrets** in the Space settings (`GROQ_API_KEY`, `HUGGINGFACEHUB_API_TOKEN`, `TAVILY_API_KEY`).
4. The app will build and launch automatically.

**Space Configuration** (from `README.md` front matter):

```yaml
sdk: streamlit
sdk_version: 1.45.1
python_version: "3.11"
app_file: app.py
```

---

## 📦 Dependencies

```
langchain
langgraph
langchain_community
langchain_core
langchain_groq
faiss_cpu
streamlit
tavily-python
huggingface_hub
```

---

## 🧱 Project Scaffold

The `setup.sh` script generates the full project directory structure from scratch:

```bash
bash setup.sh
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a pull request or file an issue.

---

## 📄 License

This project is open source. See the repository for details.

---

## 👤 Author

**Premnath Anbu**
[GitHub Profile](https://github.com/PremnathAnbu)
