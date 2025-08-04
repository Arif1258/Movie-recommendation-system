
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")


movies['genres'] = movies['genres'].str.replace('|', ' ')


tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies['genres'])


cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()


def get_recommendations(title, cosine_sim=cosine_sim):
    """Return top 10 similar movies based on genres."""
    if title not in indices:
        return []
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # top 10
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()
