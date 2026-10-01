from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import (
    Language,
    RecursiveCharacterTextSplitter,
)
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=10, chunk_overlap=3)
# texts = text_splitter.split_text("/goinfre/azebahad/RAG-against-the-machine")
# print(texts)

PYTHON_CODE = """
def hello_world():
    print("Hello, World!")

# Call the function
hello_world()
"""
python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=50, chunk_overlap=0
)
python_docs = python_splitter.create_documents([PYTHON_CODE])
print(python_docs)
