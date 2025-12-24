# stockwise/agent.py
# This file runs the Stockwise Trading Agent graph with real-time updates in the terminal.

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

import argparse
import asyncio
from stockwise.graph import stockwise_graph

async def run_stockwise(tickers):
    """
    Asynchronously executes the Stockwise graph with a list of tickers.
    """
    # Initial state as defined in our stockwise.state
    initial_state = {
        "tickers": tickers,
        "stock_data": [],
        "analysis_report": ""
    }

    print(f"🚀 Stockwise Agent started for: {', '.join(tickers)}\n")

    # Use .astream for real-time updates (perfect for terminal or React)
    async for event in stockwise_graph.astream(initial_state, stream_mode="updates"):
        # print(f"DEBUG EVENT: {event}\n")
        for node_name, output in event.items():
            if node_name == "fetch_stock_data":
                # fetch_stock_data returns {"stock_data": [snapshot]}
                stock = output["stock_data"][0]
                print(f"✅ Processed {stock['ticker']}: Price Rs.{stock['price']} | RSI: {stock['technical_indicators']['rsi']}")
            
            elif node_name == "generate_final_report":
                print(f"\n--- 📈 Stockwise FINAL REPORT ---")
                print(output["analysis_report"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stockwise Trading Agent CLI")
    parser.add_argument(
        "tickers", 
        nargs="+", 
        help="List of stock tickers (e.g., AAPL TSLA MSFT NVDA GOOGL)"
    )
    
    args = parser.parse_args()
    
    # Limit to 5 for our prototype
    input_tickers = args.tickers[:5]
    
    asyncio.run(run_stockwise(input_tickers))
    
