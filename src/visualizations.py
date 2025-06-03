import matplotlib.pyplot as plt

def plot_price_with_sma(df, sma_column='SMA_20', title='Close Price with SMA'):
    plt.figure(figsize=(14, 6))
    plt.plot(df['Date'], df['Close'], label='Close Price', alpha=0.6)
    plt.plot(df['Date'], df[sma_column], label=sma_column, alpha=0.8)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_rsi(df, rsi_column='RSI', title='RSI Indicator'):
    plt.figure(figsize=(14, 4))
    plt.plot(df['Date'], df[rsi_column], label='RSI', color='purple')
    plt.axhline(70, linestyle='--', color='red', label='Overbought (70)')
    plt.axhline(30, linestyle='--', color='green', label='Oversold (30)')
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("RSI Value")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_macd(df, macd_column='MACD', signal_column='MACD_signal', title='MACD and Signal Line'):
    plt.figure(figsize=(14, 6))
    plt.plot(df['Date'], df[macd_column], label='MACD', color='blue')
    plt.plot(df['Date'], df[signal_column], label='Signal Line', color='orange')
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("MACD Value")
    plt.legend()
    plt.grid(True)
    plt.show()
