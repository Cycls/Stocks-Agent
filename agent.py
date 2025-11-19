import cycls, os, json, yfinance as yf, plotly.graph_objects as go, dotenv
from openai import OpenAI
from ui import header, intro

dotenv.load_dotenv()
agent = cycls.Agent(keys=[os.getenv("CYCLS_KEY_1"),os.getenv("CYCLS_KEY_2")], pip=["yfinance", "plotly", "openai", "python-dotenv"], copy=[".env"])

def get_stock_data(symbol: str, period: str = "1mo"):
    stock, hist = yf.Ticker(symbol.upper()), yf.Ticker(symbol.upper()).history(period=period)
    info = stock.info
    return {"symbol": symbol.upper(), "company": info.get("longName", symbol), "price": round(info.get("currentPrice", hist['Close'].iloc[-1]), 2),
            "market_cap": info.get("marketCap"), "52w_high": info.get("fiftyTwoWeekHigh"), "52w_low": info.get("fiftyTwoWeekLow")}

def create_chart(symbol: str, chart_type: str = "candlestick"):
    hist = yf.Ticker(symbol.upper()).history(period="3mo")
    fig = go.Figure()
    if chart_type == "candlestick":
        fig.add_trace(go.Candlestick(x=hist.index, open=hist['Open'], high=hist['High'], low=hist['Low'], close=hist['Close'], name=symbol.upper()))
    else:
        fig.add_trace(go.Scatter(x=hist.index, y=hist['Close'], mode='lines', name=symbol.upper(), line=dict(width=3, color='#00d4ff')))
    fig.update_layout(title=f"📊 {symbol.upper()} - 3 Month Performance", xaxis_title="Date", yaxis_title="Price (USD)", 
                      template="plotly_dark", height=600, xaxis_rangeslider_visible=False, hovermode='x unified')
    return fig

def compare_stocks(symbol1: str, symbol2: str):
    hist1, hist2 = yf.Ticker(symbol1.upper()).history(period="3mo"), yf.Ticker(symbol2.upper()).history(period="3mo")
    norm1, norm2 = (hist1['Close'] / hist1['Close'].iloc[0] - 1) * 100, (hist2['Close'] / hist2['Close'].iloc[0] - 1) * 100
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hist1.index, y=norm1, mode='lines', name=symbol1.upper(), line=dict(width=3, color='#00d4ff')))
    fig.add_trace(go.Scatter(x=hist2.index, y=norm2, mode='lines', name=symbol2.upper(), line=dict(width=3, color='#ff6b35')))
    fig.update_layout(title=f"📊 {symbol1.upper()} vs {symbol2.upper()} - Normalized Performance", xaxis_title="Date", 
                      yaxis_title="% Change", template="plotly_dark", height=600, hovermode='x unified',
                      legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))
    return fig

def to_iframe(fig):
    html = fig.to_html(include_plotlyjs='cdn', config={'displayModeBar': True, 'responsive': True})
    return f'<iframe srcdoc="{html.replace(chr(34), "&quot;")}" width="100%" height="650" frameborder="0" style="border-radius: 8px;"></iframe>'

@agent("stocks-agent", header=header, intro=intro)
async def stock_agent(context):
    from openai import OpenAI
    dotenv.load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    messages = [{"role": "system", "content": "You're a friendly, enthusiastic stock analyst AI! 🚀 Be conversational and fun (not formal). Use emojis naturally. Keep sentences short and clean. Avoid excessive punctuation or markdown like ***___~~. Never repeat characters. Speak like a knowledgeable friend and react to the data (celebrate gains, acknowledge drops). Example: Instead of 'The stock price is $150', say 'Wow! 🚀 Apple's at $150 — looking solid!'"}]
    messages.extend([{"role": m["role"], "content": m["content"]} for m in context.messages])
    
    tools = [
        {"type": "function", "function": {"name": "get_stock_data", "description": "Get real-time stock price and key metrics",
         "parameters": {"type": "object", "properties": {"symbol": {"type": "string", "description": "Stock ticker (e.g., AAPL, TSLA)"}}, "required": ["symbol"]}}},
        {"type": "function", "function": {"name": "create_chart", "description": "Create interactive stock chart",
         "parameters": {"type": "object", "properties": {"symbol": {"type": "string"}, "chart_type": {"type": "string", "enum": ["candlestick", "line"]}}, "required": ["symbol"]}}},
        {"type": "function", "function": {"name": "compare_stocks", "description": "Compare two stocks with normalized performance",
         "parameters": {"type": "object", "properties": {"symbol1": {"type": "string"}, "symbol2": {"type": "string"}}, "required": ["symbol1", "symbol2"]}}}
    ]
    
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=tools, tool_choice="auto", temperature=0.7)
    
    if response.choices[0].message.tool_calls:
        tool_results, charts = [], []
        for tc in response.choices[0].message.tool_calls:
            fname, args = tc.function.name, json.loads(tc.function.arguments)
            if fname == "get_stock_data":
                tool_results.append({"tool": fname, "data": get_stock_data(**args)})
            elif fname == "create_chart":
                charts.append(to_iframe(create_chart(**args)))
            elif fname == "compare_stocks":
                charts.append(to_iframe(compare_stocks(**args)))
        
        if tool_results:
            # Compact tool payload and ask for narrative; ask the model to avoid noisy markdown
            compact = json.dumps(tool_results, separators=(',', ':'))
            messages.extend([{"role": "assistant", "content": f"tool_data={compact}"},
                           {"role": "user", "content": "Narrate this data in a clear, fun tone. Keep typography simple (no extra symbols)."}])
            narration = client.chat.completions.create(model="gpt-4o-mini", messages=messages, temperature=0.8)
            return narration.choices[0].message.content + ("\n\n" + "\n\n".join(charts) if charts else "")
        return "\n\n".join(charts) if charts else "Here's what I found!"
    
    return response.choices[0].message.content

agent.modal(prod=True)

