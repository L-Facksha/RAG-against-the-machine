from src.indexing.recovery import load_index
from src.retrieval.query import vectorize_query
from src.retrieval.similarity import calculate_similarity
from src.retrieval.ranking import ranking_similarity
from src.indexing.recover import recover_data
from scipy.sparse import find

index = load_index()

query = (
    "What are the default values for FP8_MIN and FP8_MAX "
    "constants in vLLM's triton_flash_attention module?"
)

# Convert the query into TF-IDF
query_vector = vectorize_query(query, index["vectorizer"])

# Calculate similarity against all indexed chunks
similarity = calculate_similarity(query_vector, index["tf_idf"])

# Rank chunks by similarity
ranked_indices = ranking_similarity(similarity)

# Display the top 10
for rank, idx in enumerate(ranked_indices[:10], start=1):
    chunk = index["chunks"][idx]

    # print(f"\n--- Rank {rank} ---")
    # print("Score:", similarity[0, idx])
    # print("File:", chunk.file_path)
    # print("Start:", chunk.first_character_index)
    # print("End:", chunk.last_character_index)

    # text = recover_data(
    #     chunk.file_path,
    #     chunk.first_character_index,
    #     chunk.last_character_index,
    # )
    # print("Content:", text[:300])
    # for idx, chunk in enumerate(index["chunks"]):
    #     if (
    #         "triton_flash_attention.py" in chunk.file_path
    #         and chunk.first_character_index == 12250
    #     ):
    #         print("Target chunk index:", idx)
    #         print("Target score:", similarity[0, idx])
    #         break

    # target_chunk = index["chunks"][13061]

    # target_text = recover_data(
    #     target_chunk.file_path,
    #     target_chunk.first_character_index,
    #     target_chunk.last_character_index,
    # )

    # for term in ["fp8_min", "fp8_max", "triton_flash_attention", "default"]:
    #     print(term, term in target_text.lower())


    # target_vector = index["tf_idf"][13061]

    # feature_names = index["vectorizer"].get_feature_names_out()

    # for term in ["fp8_min", "fp8_max"]:
    #     term_index = index["vectorizer"].vocabulary_[term]
    #     weight = target_vector[0, term_index]

    #     print(term, "weight:", weight)

    target_index = 13061
    target_vector = index["tf_idf"][target_index]

    for term in ["fp8_min", "fp8_max", "triton_flash_attention", "default"]:
        term_index = index["vectorizer"].vocabulary_[term]

        query_weight = query_vector[0, term_index]
        document_weight = target_vector[0, term_index]

        contribution = query_weight * document_weight

        print(f"\nTerm: {term}")
        print("Query weight:", query_weight)
        print("Document weight:", document_weight)
        print("Similarity contribution:", contribution)

    print("\nTotal similarity:", similarity[0, target_index])