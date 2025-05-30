from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def create_lda_pipeline(min_df=1, max_df=1.0, n_components=5, ngram_range=(1,2)):
    """
    Create an LDA pipeline. Defaults are test-friendly: min_df=1, max_df=1.0.
    """
    return Pipeline([
        ("vectorizer", CountVectorizer(
            max_df=max_df,
            min_df=min_df,
            ngram_range=ngram_range,
            stop_words="english"
        )),
        ("lda", LatentDirichletAllocation(
            n_components=n_components,
            learning_method="online",
            batch_size=128,
            max_iter=10,
            random_state=0,
            n_jobs=-1
        ))
    ])

def fit_lda_pipeline(pipeline, headlines):
    return pipeline.fit(headlines)

def extract_topics(model, feature_names, n_top=8):
    topics = []
    for topic_weights in model.components_:
        top_terms = [feature_names[i] for i in topic_weights.argsort()[:-n_top - 1:-1]]
        topics.append(top_terms)
    return topics

def get_feature_names(pipeline):
    return pipeline.named_steps["vectorizer"].get_feature_names_out()

def get_lda_model(pipeline):
    return pipeline.named_steps["lda"]
