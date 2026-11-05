from src.retrieval.similarity import calculate_similarity
from src.retrieval.retriever import retrieve_top_k
from src.retrieval.ranking import ranking_similarity
from src.chunking.chuncker import Chunk
from src.indexing.recovery import load_index


def augment_prompt(question: str, retrieved_text: list[str]) -> str:
    instructions = """
SYSTEM_INSTRUCTION:\n
You are a technical assistant specialized in answering questions
about the vLLM project.\n
Your task is to answer the user's question using the provided context.\n
Rules:\n
1. Use the retrieved context as the primary source of information.\n
2. Do not invent functions, classes, methods, parameters, commands,
file paths, or configuration options.\n
3. Do not introduce information that contradicts the provided context.\n
4. If the context does not contain enough information to answer,
clearly state that the available context is insufficient.\n
5. If only part of the question can be answered, explain what
is supported by the context and identify what is missing.\n
6. Preserve technical names, code identifiers, and configuration
values exactly as they appear in the context.\n
7. Explain technical concepts clearly and provide examples only
when they are supported by the context.\n
8. Do not claim that something exists or works unless the context
provides evidence for it.\n
Keep your answer clear, accurate, and relevant to the question.\n
"""
    context = "\n\n".join(retrieved_text)

    instructions += "\n\nCONTEXT:\n\n" + context
    instructions += "\n\nQUESTION:\n\n" + question

    return instructions


# ss = ["kjdhdkjfh", "fhkj", "kfgkgskf"]
# ll = augment_prompt("hello", ss)
# print(ll)
