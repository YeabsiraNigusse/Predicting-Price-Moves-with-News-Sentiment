import matplotlib.pyplot as plt

def plot_indicators(df, title=''):
    plt.figure(figsize=(14, 6))
    plt.plot(df['close'], label='Close Price', alpha=0.5)
    plt.plot(df['SMA_20'], label='SMA 20', linestyle='--')
    plt.plot(df['SMA_50'], label='SMA 50', linestyle='--')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()