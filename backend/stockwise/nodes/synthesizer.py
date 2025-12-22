# synapse/agents/nodes/synthesizer.py
# Synthesizer Node: Aggregates the 5 stock snapshots and picks a winner.

from langchain_openai import ChatOpenAI
from stockwise.state import SynapseState

def generate_final_report(state: SynapseState):
    """
    Synthesizer Node: Aggregates the 5 stock snapshots and picks a winner.
    """
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    # 1. Format the data for the prompt
    # We turn the list of dicts into a readable string for the LLM
    stocks_summary = ""
    for stock in state["stock_data"]:
        stocks_summary += (
            f"\n- {stock['ticker']}: Price Rs.{stock['price']}, "
            f"RSI: {stock['technical_indicators']['rsi']}, "
            f"Trend: {stock['technical_indicators']['trend']}, "
            f"P/E: {stock['pe_ratio']}, "
            f"Market Cap: {stock['market_cap']}, "
            f"Volatility: {round((max(stock['daily_returns']) - min(stock['daily_returns'])) * 100, 2)}%\n"
        )
        print(f"DEBUG: Stock Summary for {stock['ticker']}: {stocks_summary}")

    # 2. Craft the System Prompt
    system_prompt = (
        "You are the Synapse Strategic Analyst. "
        "Review the technical and fundamental data for these 5 stocks. "
        "Identify the stock with the best risk/reward profile (e.g., strong trend but not overbought). "
        "Provide a 'Top Pick' and a brief 3-sentence justification."
    )

    # 3. Invoke the LLM
    response = llm.invoke([
        ("system", system_prompt),
        ("human", f"Here is the market data: {stocks_summary}")
    ])

    # 4. Update the State
    # Note: We return the decision and the report to the global state
    return {
        "analysis_report": response.content,
        "decision": response.content.split('\n')[0] # Simple extraction logic
    }
