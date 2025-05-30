import talib

def add_indicators(df):
    """
    Adds RSI, MACD, and Moving Averages to the DataFrame.
    """
    df['RSI'] = talib.RSI(df['close'])
    df['SMA_20'] = talib.SMA(df['close'], timeperiod=20)
    df['SMA_50'] = talib.SMA(df['close'], timeperiod=50)
    macd, macdsignal, _ = talib.MACD(df['close'])
    df['MACD'] = macd
    df['MACD_signal'] = macdsignal
    return df