import pandas as pd

def extract_publisher_domain(news_df):
    mask_email = news_df["publisher"].str.contains("@", na=False)
    news_df.loc[mask_email, "publisher_domain"] = news_df.loc[mask_email, "publisher"].str.split("@").str[1]
    return news_df

def top_publishers(news_df, n=10):
    # value_counts gives a Series named 'count'
    vc = news_df["publisher"].value_counts().head(n)
    df = vc.reset_index()
    df.columns = ["publisher", "n_articles"]
    return df

def top_publisher_domains(news_df, n=10):
    return news_df["publisher_domain"].value_counts().head(n)
