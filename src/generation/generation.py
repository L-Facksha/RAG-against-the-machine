from transformers import AutoModelForCausalLM, AutoTokenizer
from src.generation.augmentation import augment_prompt
from src.retrieval.retriever import retrieve_top_k
from src.indexing.recovery import load_index
from src.retrieval.query import vectorize_query
from src.retrieval.similarity import calculate_similarity
from src.retrieval.ranking import ranking_similarity


def generate_answer(prompt: str) -> str:
    model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-0.6B")
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-0.6B")
    tokens = tokenizer(prompt, return_tensors="pt")
    output = model.generate(**tokens, max_new_tokens=100)
    output = output[:, tokens["input_ids"].shape[1]:]
    output = tokenizer.decode(output[0], skip_special_tokens=True)
    return output


# index = load_index()
# vectorize_ques = vectorize_query("What is the capital of Japan?", index['vectorizer'])
# similarity = calculate_similarity(vectorize_ques, index['tf_idf'])
# sorted_similarity = ranking_similarity(similarity)
# retrieve, _ = retrieve_top_k(1, sorted_similarity, index['chunks'])
# print("retrieve: ", retrieve)
# prompt = augment_prompt("What is the capital of Japan?", retrieve)
# print(generate_answer(prompt))
