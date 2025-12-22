# synapse/agents/graph.py
# This file constructs the StateGraph for the Synapse Trading Agent using LangGraph.

from langgraph.graph import StateGraph, START, END
from langgraph.constants import Send
from stockwise.state import SynapseState
from stockwise.nodes.stock_worker import fetch_stock_data
from stockwise.nodes.synthesizer import generate_final_report

# 1. The Mapping Logic (Orchestrator)
def orchestrate_stocks(state: SynapseState):
    """
    Conditional edge logic: 
    Takes the list of tickers and 'Sends' them to parallel workers.
    """
    return [Send("fetch_stock_data", {"ticker_symbol": ticker}) for ticker in state["tickers"]]

# 2. Build the Graph
builder = StateGraph(SynapseState)

# Add Nodes
# The 'fetch_stock_node' is actually your fetch_stock_data function
builder.add_node("fetch_stock_data", fetch_stock_data)
builder.add_node("generate_final_report", generate_final_report)

# 3. Define the Flow
# Start -> Orchestrator (Conditional) -> Parallel Fetching -> Synthesizer -> End
builder.add_conditional_edges(
    START,
    orchestrate_stocks,
    {"fetch_stock_data": "fetch_stock_data"}
)

# Once ALL parallel fetch nodes are done, they automatically 'join' to the synthesizer
builder.add_edge("fetch_stock_data", "generate_final_report")
builder.add_edge("generate_final_report", END)

# 4. Compile
synapse_graph = builder.compile()
