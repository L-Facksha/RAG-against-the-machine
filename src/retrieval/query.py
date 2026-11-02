from sklearn.feature_extraction.text import TfidfVectorizer
from src.indexing.recovery import load_index


def vectorize_query(ques: str, victorizer: TfidfVectorizer) -> TfidfVectorizer:
    ques_vector = victorizer.transform([ques])
    return ques_vector


# index = load_index()
# print(index.keys())
# print(vectorize_query("what's ur name", index['vectorizer']))
