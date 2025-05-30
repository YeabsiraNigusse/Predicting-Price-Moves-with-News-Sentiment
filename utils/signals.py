def generate_signals(df):
    """
    Create basic Buy/Sell signals using SMA crossovers.
    """
    df['Signal'] = 0
    df.loc[df['SMA_20'] > df['SMA_50'], 'Signal'] = 1
    df.loc[df['SMA_20'] < df['SMA_50'], 'Signal'] = -1
    return df