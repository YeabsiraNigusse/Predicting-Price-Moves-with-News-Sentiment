import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pandas as pd
from src.descriptive_stats import (
    load_news_data, add_headline_length_features, compute_headline_stats
)
from src.publisher_analysis import (
    extract_publisher_domain, top_publishers, top_publisher_domains
)
from src.date_analysis import (
    parse_dates, daily_article_counts
)
from src.topic_modeling import (
    create_lda_pipeline, fit_lda_pipeline, extract_topics, get_feature_names, get_lda_model
)

class TestNewsAnalysis(unittest.TestCase):
    def setUp(self):
        self.sample_data = pd.DataFrame({
            "date": ["2021-01-01", "2021-01-02"],
            "headline": ["Big news today", "Something happened"],
            "publisher": ["nytimes", "editor@domain.com"]
        })

    def test_add_headline_length_features(self):
        df = add_headline_length_features(self.sample_data.copy())
        self.assertIn("headline_len_chars", df.columns)
        self.assertIn("headline_len_words", df.columns)
        self.assertEqual(df["headline_len_words"].iloc[0], 3)

    def test_extract_publisher_domain(self):
        df = extract_publisher_domain(self.sample_data.copy())
        self.assertEqual(df["publisher_domain"].iloc[1], "domain.com")

    def test_top_publishers(self):
        sample_df = pd.DataFrame({
            "publisher": ["A", "B", "A", "C", "B", "A"]
        })
        df = top_publishers(sample_df)
        self.assertEqual(df.shape[1], 2)
        self.assertEqual(df.columns.tolist(), ["publisher", "n_articles"])

    def test_parse_dates_and_resample(self):
        df = parse_dates(self.sample_data.copy())
        resampled = daily_article_counts(df)
        self.assertEqual(resampled.shape[0], 2)

    def test_topic_modeling_pipeline(self):
        headlines = [
            "Stocks rally as inflation cools",
            "Inflation data boosts market sentiment",
            "Tech stocks lead Wall Street gains",
            "Investors eye Federal Reserve meeting",
            "Wall Street closes higher on strong earnings",
            "Oil prices fall amid global growth concerns",
            "Crypto market rebounds after recent losses",
            "Economy shows signs of slowing",
            "Consumer confidence rises unexpectedly",
            "Retail sales beat expectations"
        ]
        pipeline = create_lda_pipeline()
        fitted_pipeline = fit_lda_pipeline(pipeline, headlines)
        features = get_feature_names(fitted_pipeline)
        lda_model = get_lda_model(fitted_pipeline)
        topics = extract_topics(lda_model, features)
        self.assertIsInstance(topics, list)
        self.assertTrue(all(isinstance(t, list) for t in topics))

if __name__ == "__main__":
    unittest.main()
