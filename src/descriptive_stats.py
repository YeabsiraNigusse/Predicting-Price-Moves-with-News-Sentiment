import pandas as pd

def load_news_data(path):
    try:
        news = pd.read_csv(path, parse_dates=["date"])
        return news
    except Exception as e:
        raise IOError(f"Error loading data: {e}")

def add_headline_length_features(news_df):
    news_df["headline_len_chars"] = news_df["headline"].str.len()
    news_df["headline_len_words"] = news_df["headline"].str.split().str.len()
    return news_df

def compute_headline_stats(news_df):
    return news_df[["headline_len_chars", "headline_len_words"]].describe()

