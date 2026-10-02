# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_text_splitters import (
#     Language,
#     RecursiveCharacterTextSplitter,
# )
# # text_splitter = RecursiveCharacterTextSplitter(chunk_size=10, chunk_overlap=3)
# # texts = text_splitter.split_text("/goinfre/azebahad/RAG-against-the-machine")
# # print(texts)

# PYTHON_CODE = """
# def hello_world():
#     print("Hello, World!")

# # Call the function
# hello_world()
# """
# python_splitter = RecursiveCharacterTextSplitter.from_language(
#     language=Language.PYTHON, chunk_size=50, chunk_overlap=0
# )
# python_docs = python_splitter.create_documents([PYTHON_CODE])
# print(python_docs)

from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

PYTHON_CODE = """
def add(a, b):
    return a + b

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, value):
        self.result += value
        return self.result

    def subtract(self, value):
        self.result -= value
        return self.result

# Call the function
def main():
    calc = Calculator()
    print(calc.add(5))
    print(calc.subtract(2))

if __name__ == "__main__":
    main()
"""
python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=100, chunk_overlap=0)

python_docs = python_splitter.create_documents([PYTHON_CODE])
print(python_docs)
