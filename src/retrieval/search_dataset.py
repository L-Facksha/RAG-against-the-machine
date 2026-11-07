from src.chunking.chuncker import Chunk
from src.indexing.recovery import load_index
from src.retrieval.retriever import retrieve_top_k
from src.retrieval.similarity import calculate_similarity
from src.retrieval.query import vectorize_query
from src.retrieval.ranking import ranking_similarity
from src.indexing.recover import recover_data
from src.models.models import RagDataset, MinimalSearchResults, StudentSearchResults, MinimalSource
from pathlib import Path
import json


def search_dataset(path_dataset: str, k: int, saved_path: str):
    # repo_root = Path.cwd()  # Get the root directory of the project
    path = Path(Path.cwd() / path_dataset)
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        dataset = RagDataset.model_validate(data)
    except json.JSONDecodeError as e:
        print(f"Error at line {e.lineno}, col {e.colno}.")
        return None

    index = load_index()
    search_result = []
    for ques in dataset.rag_questions:
        minimal_source: list[MinimalSource] = []
        vectorize_ques = vectorize_query(ques.question, index['vectorizer'])
        similarity = calculate_similarity(vectorize_ques, index['tf_idf'])
        sorted_similarity = ranking_similarity(similarity)
        retrieve, chunks = retrieve_top_k(
            k, sorted_similarity, index['chunks'])
        for chunk in chunks:
            source = MinimalSource(
                file_path=chunk.file_path,
                first_character_index=chunk.first_character_index,
                last_character_index=chunk.last_character_index
            )
            minimal_source.append(source)
        minimalsearchresult = MinimalSearchResults(
            question_id=ques.question_id,
            question=ques.question,
            retrieved_sources=minimal_source
        )
        search_result.append(minimalsearchresult)
    student_search = StudentSearchResults(
        search_results=search_result,
        k=k
    )
    path_for_save = Path(Path.cwd() / saved_path)
    path_for_save.parent.mkdir(parents=True, exist_ok=True)
    with open(path_for_save, "w", encoding="utf-8") as f:
        json.dump(student_search.model_dump(), f, indent=4, ensure_ascii=False)


# print(search_dataset())
result = search_dataset(
    path_dataset="data/raw/datasets_public/public/UnansweredQuestions/dataset_code_public.json",
    k=5,
    saved_path="data/output/search_results/UnansweredQuestions/dataset_code_public.json"
)

print(result)