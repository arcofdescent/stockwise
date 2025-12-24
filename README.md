# 🧠 Stockwise

**Stockwise** is an open-source, agentic AI-powered stock research and analysis engine.  
It leverages Python, [LangGraph](https://github.com/langchain-ai/langgraph), and React to fetch, analyze, and synthesize insights from real market data.

- ⚡ Modular node-by-node finance analysis workflow (LangGraph)
- 🏦 Supports Indian and global equities (via yfinance, broker APIs)
- 🧾 Generates synthesized buy/sell reports (for educational use only!)
- 📊 Interactive dashboard (React frontend)
- 🤝 100% open source—contributions welcome!

---

## 🚀 Quick Start

Make sure you have `uv` installed. 
Docs to install uv from [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/).

Then, clone the repo and run the backend and frontend:

```bash
git clone https://github.com/arcofdescent/stockwise.git
cd stockwise/backend
uv venv
source .venv/bin/activate
uv sync --dev
```

We currently support OpenAI API, so add your key to .env (or add to your environment variables):

```
OPENAI_API_KEY="your_openai_api_key_here"
```

Example run commands:

* Run the agent for stock analysis:

```bash
python -m stockwise.agent INFY.NS IOC.NS TCS.NS # Analyze Infosys, Indian Oil, TCS stocks
```

## 🛡️ Disclaimer

> Stockwise is a research and learning tool. It is not investment advice.  
Use at your own risk and always conduct your own research before making investment decisions.

---

## 🏗️ Features/Milestones

- [x] Modular backend with LangGraph nodes for:
  - Fetching stock data (yfinance, broker APIs)
  - Technical/fundamental analysis
  - Synthesis and report generation
- [ ] React frontend dashboard:
  - Upload watchlist/holdings
  - Visualize trends, signals & reports
- [ ] Pluggable API system (easy to add new brokers)
- [ ] Documentation & demo workflows
- [ ] Testing & CI/CD integration

## 🧑‍💻 Contributing

Pull requests, issues, and feature ideas are welcome!  
See [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

---

## 📝 License

[MIT](./LICENSE)
