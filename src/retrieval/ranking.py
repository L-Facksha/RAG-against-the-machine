import numpy as np
from src.retrieval.similarity import calculate_similarity
from src.retrieval.query import vectorize_query
from src.indexing.recovery import load_index


def ranking_similarity(similarity: np.ndarray) -> np.ndarray:
    sorted = np.argsort(similarity)
    return sorted[0][::-1]


# index = load_index()
# vectorize_ques = vectorize_query(
#     "How to configure OpenAI server?", index['vectorizer'])
# similarity = calculate_similarity(vectorize_ques, index['tf_idf'])
# sorted_similarity = ranking_similarity(similarity)
# print(sorted_similarity)
# print(similarity[0][sorted_similarity])
# # sorted_similarity = sorted_similarity[0][::-1]
# # print(sorted_similarity)
# # print(similarity[0][sorted_similarity])
# print("argmax: ", np.argmax(similarity))

# print(similarity[0][1023])
# chunks = index['chunks']
# print(chunks[1023])
