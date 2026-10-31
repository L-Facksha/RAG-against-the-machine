from sklearn.feature_extraction.text import TfidfVectorizer
from src.indexing.preparation import preparation_data
from src.chunking.chuncker import Chunk
from scipy.sparse import csc_matrix


def vectorize_data(directory: str, max_size: int) -> tuple[
    csc_matrix, TfidfVectorizer, list[Chunk]
]:
    recovered_data, chunks = preparation_data(directory, max_size)
    vectorizer = TfidfVectorizer()
    tf_idf = vectorizer.fit_transform(recovered_data)

    return tf_idf, vectorizer, chunks

