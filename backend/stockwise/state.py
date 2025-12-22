# synpase/agents/state.py
# This file defines the global state structure using LangGraph's TypedDict and Annotated features.

import operator
from typing import Annotated, TypedDict, List, Dict, Any, Union

class StockSnapshot(TypedDict):
    """The data structure for a single stock's analysis."""
    ticker: str
    price: float
    pe_ratio: Union[float, None]
    market_cap: int
    daily_returns: List[float]  # Used for volatility calc
    technical_indicators: Dict[str, Any]  # RSI, SMA, etc.
    sentiment_score: float  # If you add news later

class SynapseState(TypedDict):
    """The global state for the Synapse Trading Agent."""
    # Input: What we want to track
    tickers: List[str]
    
    # Aggregated Data: The Reducer 'operator.add' is the secret sauce.
    # It ensures parallel workers append to this list instead of overwriting.
    stock_data: Annotated[List[StockSnapshot], operator.add]
    
    # Final Output
    analysis_report: str
    decision: str  # e.g., "BUY", "HOLD", "SELL" (Top Pick)
    
