from src.chunking.chuncker import Chunk
from src.indexing.recovery import load_index
from src.retrieval.query import vectorize_query
from src.retrieval.similarity import calculate_similarity
from src.retrieval.ranking import ranking_similarity
from src.indexing.recover import recover_data
import numpy as np


def retrieve_top_k(k: int, ranked_indices: np.ndarray,
                   chunks: list[Chunk]) -> tuple[list[str], list[Chunk]]:
    if k <= 0:
        print("ERROR: K must be > 0")
        return None
    chunks_data: list[Chunk] = []
    indices = ranked_indices[:k]
    chunks_data.extend([chunks[index] for index in indices])

    retrieve_text: list[str] = []
    for chunk in chunks_data:
        retrieve_text.append(recover_data(
            chunk.file_path, chunk.first_character_index,
            chunk.last_character_index
        ))

    return retrieve_text, chunks_data


# index = load_index()
# vectorize_ques = vectorize_query(
#     "How to configure OpenAI server?", index['vectorizer'])
# similarity = calculate_similarity(vectorize_ques, index['tf_idf'])
# sorted_similarity = ranking_similarity(similarity)
# retrive, _ = retrieve_top_k(1, sorted_similarity, index['chunks'])
# for x in range(len(retrive)):
#     print(f"{x}: {retrive[x]}\n")
#     print("*" * 200)
