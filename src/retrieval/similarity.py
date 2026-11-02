# from src.retrieval.query import vectorize_query
# from src.indexing.recovery import load_index
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
import numpy as np


def calculate_similarity(question_vector: csr_matrix,
                         tf_idf: csr_matrix) -> np.ndarray:
    similarity = cosine_similarity(question_vector, tf_idf)
    return similarity


# index = load_index()
# vectorize_ques = vectorize_query("How to configure OpenAI server?", index['vectorizer'])
# calculate_similarity(vectorize_ques, index['tf_idf'])
