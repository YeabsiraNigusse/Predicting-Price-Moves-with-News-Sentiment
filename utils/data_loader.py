from pynance import get_history

def fetch_stock_data(symbol: str, start: str, end: str):
    """
    Fetch historical stock data using PyNance.
    Example symbol: 'AAPL'
    """
    df = get_history(symbol, start=start, end=end)
    df.index = df.index.date  # Optional: make index more readable
    return df