# 💼 Financial Agentic AI Application

A multi-agent AI application that leverages **Groq-powered LLMs** with financial tools and real-time web search capabilities to analyze stock market data, provide financial summaries, and deliver up-to-date company insights.

---

## 🧠 Overview

This project demonstrates how to build an **Agentic AI system** using the [phi](https://pypi.org/project/phi-agent/) framework, integrating multiple specialized agents:

* A **Web Search Agent** that fetches real-time information from the internet.
* A **Finance AI Agent** that provides stock prices, analyst recommendations, fundamentals, and news using Yahoo Finance data.
* A **Coordinator Agent** that combines the knowledge and capabilities of both.

---

## ⚙️ Features

* 📈 Real-time stock data and financial analysis (via Yahoo Finance).
* 🌐 Real-time web search with source attribution (via DuckDuckGo).
* 🤖 Multi-agent collaboration using the `phi` agent framework.
* 🧾 Output in readable, markdown-formatted text with tables and sources.

---

## 📦 Requirements

* Python 3.8+
* [phi](https://pypi.org/project/phi-agent/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/financial-agentic-ai.git
   cd financial-agentic-ai
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory and add your Groq API key:

   ```
   PHI_API_KEY=your_phi_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

---

## 🚀 Running the App

To run the multi-agent AI and ask for a financial summary, execute:

```python
python financial_agent.py
```



---

## 🧩 Agents Overview

### 🔍 Web Search Agent

* **Purpose:** Searches the web for relevant information.
* **Tool:** DuckDuckGo
* **Instruction:** Always include sources.

### 💰 Finance AI Agent

* **Purpose:** Analyzes financial data from Yahoo Finance.
* **Tools:**

  * Stock Prices
  * Analyst Recommendations
  * Company Fundamentals
  * Latest News
* **Instruction:** Use tables to display financial data.

### 🧠 Multi-Agent Coordinator

* **Combines** both Web and Finance agents to deliver comprehensive insights in a single response.

---

## 📁 File Structure

```bash
financial-agentic-ai/
│
├── financial_agent.py          # Main script that runs the multi-agent system
├── .env             # Contains GROQ_API_KEY
├── README.md        # Project documentation
└── requirements.txt # List of dependencies
```

---

## 📜 License

MIT License. See `LICENSE` file for details.

---

## 🙌 Acknowledgements

* [Phi Agent Framework](https://github.com/Prompt-Engineering/phi)
* [Groq](https://groq.com/)
* [Yahoo Finance](https://finance.yahoo.com/)
* [DuckDuckGo](https://duckduckgo.com/)


