# stockwise/nodes/stock_worker.py
# This file defines the worker node that fetches and processes stock data for a given ticker.

import yfinance as yf
import pandas as pd
import talib as ta
import numpy as np
from stockwise.state import StockSnapshot

def fetch_stock_data(input_data: dict) -> dict:
    ticker_symbol = input_data["ticker_symbol"]
    ticker = yf.Ticker(ticker_symbol)
    
    # 1. Fetch Data
    info = ticker.info
    df = ticker.history(period="3mo")
    
    if df.empty:
        return {"stock_data": []}

    # --- TA-Lib Integration ---
    # Convert 'Close' to a numpy array for TA-Lib
    close_prices = df['Close'].values

    # SMA 20 using TA-Lib
    # Note: TA-Lib returns a numpy array of the same length
    df['SMA_20'] = ta.SMA(close_prices, timeperiod=20)
    
    # RSI 14 using TA-Lib
    df['RSI'] = ta.RSI(close_prices, timeperiod=14)

    # MACD
    macd, macdsignal, macdhist = ta.MACD(close_prices, fastperiod=12, slowperiod=26, signalperiod=9)
    df['MACD'] = macd
    df['MACD_Signal'] = macdsignal
    df['MACD_Hist'] = macdhist

    # Get the latest row
    latest = df.iloc[-1]
    
    # --- Data Serialization Cleanup ---
    # Cast numpy.float64 to standard float for JSON/React compatibility
    def clean_val(val):
        if pd.isna(val) or val is None:
            return None
        return float(val)

    snapshot: StockSnapshot = {
        "ticker": ticker_symbol,
        "price": clean_val(latest['Close']),
        "pe_ratio": clean_val(info.get("forwardPE")),
        "market_cap": info.get("marketCap"),
        "daily_returns": [clean_val(r) for r in df['Close'].pct_change().tail(5).tolist()],
        "technical_indicators": {
            "rsi": clean_val(latest['RSI']),
            "sma_20": clean_val(latest['SMA_20']),
            "macd": clean_val(latest['MACD']),
            "macd_signal": clean_val(latest['MACD_Signal']),
            "macd_hist": clean_val(latest['MACD_Hist']),
            "pe_trend": "Bullish" if latest['MACD'] > latest['MACD_Signal'] else "Bearish",
            "rsi_trend": "Overbought" if latest['RSI'] > 70 else ("Oversold" if latest['RSI'] < 30 else "Neutral"),
            "trend": "Bullish" if latest['Close'] > latest['SMA_20'] else "Bearish"
        },
        "sentiment_score": 0.0
    }

    return {"stock_data": [snapshot]}

