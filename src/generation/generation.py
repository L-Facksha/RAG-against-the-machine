from transformers import AutoModelForCausalLM, AutoTokenizer
from src.generation.augmentation import augment_prompt


def generate_answer(prompt: str) -> str:
    model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-0.6B")
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-0.6B")
    tokens = tokenizer(prompt, return_tensors="pt")
    output = model.generate(**tokens, max_new_tokens=100)
    return output[:, tokens["input_ids"].shape[1]:]


ss = ["kjdhdkjfh", "fhkj", "kfgkgskf"]
prompt = augment_prompt("hello", ss)
print(generate_answer(prompt))
