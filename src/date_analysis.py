import pandas as pd

def parse_dates(news_df):
    news_df["date"] = pd.to_datetime(news_df["date"], utc=True, format="ISO8601")
    return news_df.set_index("date")

def daily_article_counts(news_df):
    return news_df.resample("D").size().rename("n_articles")
