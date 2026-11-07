from src.generation.augmentation import augment_prompt
from src.generation.generation import generate_answer
from src.indexing.recover import recover_data
from src.models.models import StudentSearchResults, MinimalAnswer, StudentSearchResultsAndAnswer
from pathlib import Path
import json


def answer_dataset(student_search_results_path: str, save_directory: str):
    path = Path(Path.cwd() / student_search_results_path)

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        dataset = StudentSearchResults.model_validate(data)
    except json.JSONDecodeError as e:
        print(f"Error at line {e.lineno}, col {e.colno}.")
        return None

    answer = []
    for ques in dataset.search_results:
        retrieved_data: list[str] = []
        for retrieve in ques.retrieved_sources:
            retrieved_data.append(recover_data(
                retrieve.file_path, retrieve.first_character_index, retrieve.last_character_index
            ))
        instructions = augment_prompt(ques.question, retrieved_data)
        answer.append(MinimalAnswer(
            question_id=ques.question_id,
            question=ques.question,
            answer=generate_answer(instructions),
            retrieved_sources=ques.retrieved_sources
        ))
    student_s_result = StudentSearchResultsAndAnswer(
        search_results=answer,
        k=dataset.k
    )
    path_for_save = Path(Path.cwd() / save_directory)
    path_for_save.parent.mkdir(parents=True, exist_ok=True)
    with open(path_for_save, "w", encoding="utf-8") as f:
        json.dump(student_s_result.model_dump(),
                  f, indent=4, ensure_ascii=False)
    return student_s_result


if __name__ == "__main__":
    result = answer_dataset(
        student_search_results_path="data/output/search_results/UnansweredQuestions/dataset_code_public.json",
        save_directory="data/output/search_results_and_answer/UnansweredQuestions/dataset_docs_public.json"
    )
    print(result)
