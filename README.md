# Stocks Agent

A conversational AI that provides real-time stock data, technical analysis, and interactive charts.

**Live Demo:** `https://stock-agent-280879789566.me-central1.run.app/`

---

## 🎯 About The Project

This agent acts as a friendly stock analyst, making financial data accessible and easy to understand. It uses **GPT-4o-mini** to interpret user requests and orchestrate a suite of powerful financial analysis tools. The agent leverages the **yfinance** library to fetch live market data and **Plotly** to generate rich, interactive visualizations, including:
-   Real-time price and key metric lookups.
-   Candlestick and line charts for performance analysis.
-   Normalized comparison charts for multiple stocks.
-   A full technical dashboard with Moving Averages (MAs), Volume, and RSI.

The final output combines a fun, conversational narrative with detailed, interactive charts.

## 🛠️ Tech Stack

-   **Framework**: [Cycls](https://cycls.com/)
-   **Language**: Python
-   **APIs & Libraries**:
    -   **OpenAI API (GPT-4o-mini)**: For conversational logic and tool use.
    -   **yfinance**: For fetching historical and real-time stock market data.
    -   **Plotly**: For creating interactive data visualizations and charts.

## 🚀 Getting Started

To run this project locally, clone the repository, create a `.env` file with your API keys, install dependencies, and run the agent.

```bash
# 1. Clone the repository
git clone [https://github.com/your-username/stocks-agent.git](https://github.com/your-username/stocks-agent.git)
cd stock-analysis-agent

# 2. Create and populate your .env file
# Example: echo "OPENAI_API_KEY=sk-..." > .env
# Required keys: CYCLS_API_KEY, OPENAI_API_KEY
```
## Make the AI you love, Cycls does the rest.
