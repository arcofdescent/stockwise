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
python main.py

# In a separate terminal
cd ../frontend
npm install
npm run dev
```

## 🧩 Project Structure

```
stockwise/
  backend/         # Python: data fetching, analysis, LangGraph nodes
    main.py
    pyproject.toml
	stockwise/
	  nodes/
		data_fetching.py
		analysis.py
		synthesis.py
	  utils/
		helpers.py
  frontend/        # React: UI, charts, reports
    src/
      App.jsx
      index.js
    package.json
  docs/            # Additional documentation/assets
  tests/           # Test suites (coming soon)
  .github/         # Templates for issues, PRs, workflows
    ISSUE_TEMPLATE.md
    PULL_REQUEST_TEMPLATE.md
  README.md
  LICENSE
  CONTRIBUTING.md
  .gitignore
```

## 🛡️ Disclaimer

> Stockwise is a research and learning tool. It is not investment advice.  
Use at your own risk and always conduct your own research before making investment decisions.

---

## 🏗️ Features/Milestones

- [ ] Modular backend with LangGraph nodes for:
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
