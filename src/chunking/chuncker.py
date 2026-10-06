from pathlib import Path
import ast

from src.models.models import MinimalSource
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

from typing import Optional

class Chunk(MinimalSource):
    content: str
    name: Optional[str] = None
    parent: Optional[str] = None


def python_chunker(path: Path, max_size: int) -> tuple[list[Chunk], str]:
    with open(path, "r", encoding="utf-8") as f:
        # source = f.read()
        source = path.read_text(encoding="utf-8")

        print(repr(source[0:40]))
        print("char at index 24:", repr(source[24]))
        print("char at index 25:", repr(source[25]))

    python_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON,
        chunk_size=max_size,
        chunk_overlap=0,
        add_start_index=True,  # gives the real position directly, no .find() needed
    )
    python_docs = python_splitter.create_documents([source])

    all_chunks: list[Chunk] = []
    for doc in python_docs:
        first_character_index = doc.metadata["start_index"]
        last_character_index = first_character_index + len(doc.page_content) - 1
        print("First: ", first_character_index)
        print("Last: ", last_character_index)

        all_chunks.append(
            Chunk(
                file_path=str(path),
                first_character_index=first_character_index,
                last_character_index=last_character_index,
                content=doc.page_content,
            )
        )

    return all_chunks, source


def main():
    directory = Path("/home/piziga/RAG-against-the-machine/test_body.py")
    chunks, source = python_chunker(directory, 100)

    for chunk in chunks:
        assert source[chunk.first_character_index: chunk.last_character_index + 1] == chunk.content
    print(f"all {len(chunks)} offsets verified correct")


if __name__ == "__main__":
    main()

# def python_chunker(path: Path, max_size: int) -> list[MinimalSource]:
#     all_chunks: list[MinimalSource] = []

#     # print(path)
#     # for file_path in path:
#     with open(path, "r") as f:
#         source = f.read()

#     python_splitter = RecursiveCharacterTextSplitter.from_language(
#         language=Language.PYTHON, chunk_size=max_size, chunk_overlap=0)
#     python_docs = python_splitter.create_documents([source])
#     for doc in python_docs:
#         first_character_index = source.find(doc.page_content)
#         # print("First: ", first_character_index)
#         # print(len(repr(doc.page_content)))
#         last_character_index = first_character_index + len(doc.page_content)
#         # print("Last: ", last_character_index)
#         # print("Content:", repr(doc.page_content))

#         # all_chunks.append(doc.page_content)
#         all_chunks.append(
#             MinimalSource(
#                 file_path=str(path),
#                 first_character_index=first_character_index,
#                 last_character_index=last_character_index,
#             )
#         )

#     return all_chunks


# def main():
#     directory = Path("/home/piziga/RAG-against-the-machine/test_body.py")

#     chunks = python_chunker(directory, 100)
#         for chunk in chunks:
#             assert source[chunk.first_character_index : chunk.last_character_index + 1] == chunk.content
#         print("all offsets verified correct")

#     # print("Python code chunks:\n\n", chunks)


# if __name__ == "__main__":
#     main()


# def get_character_index(source: str, line: int, column: int) -> int:
#     lines = source.splitlines(keepends=True)
#     # print(lines)

#     return sum(len(current_line) for current_line in lines[:line - 1]) + column

# from pathlib import Path

# import ast

# from src.models.models import MinimalSource


# # def split_large_node(source, node, max_size):
# #     tree = ast.parse(source)
# #     for node in ast.walk(tree):
# #         if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
# #             first_character_index = get_character_index(
# #                 source,
# #                 node.lineno,
# #                 node.col_offset
# #             )
# #             end_character_index = get_character_index(
# #                 source,
# #                 node.end_lineno,
# #                 node.end_col_offset
# #             )


# def get_character_index(source: str, line: int, column: int) -> int:
#     lines = source.splitlines(keepends=True)
#     # print(lines)

#     return sum(len(current_line) for current_line in lines[:line - 1]) + column


# def python_chunker(path: Path, max_size: int) -> list[MinimalSource]:
#     all_chunks: list[MinimalSource] = []

#     print(path)

#     for file_path in path.glob("**/*.py"):
#         with open(file_path, "r") as f:
#             source = f.read()

#         try:
#             tree = ast.parse(source)
#         except SyntaxError:
#             continue

#         for node in ast.walk(tree):

#             if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):

#                 first_character_index = get_character_index(
#                     source,
#                     node.lineno,
#                     node.col_offset
#                 )

#                 end_character_index = get_character_index(
#                     source,
#                     node.end_lineno,
#                     node.end_col_offset
#                 )

#                 last_character_index = end_character_index - 1

#                 # node is small enough
#                 if last_character_index - first_character_index < 2000:
#                     all_chunks.append(
#                         MinimalSource(
#                             file_path=str(file_path),
#                             first_character_index=first_character_index,
#                             last_character_index=last_character_index,
#                         )
#                     )
#                     continue

#                 # node is too large
#                 for statment in node.body:

#                     # print(first_character_index)
#                     # print(last_character_index)
#                     # print(hasattr(statment, "body"))

#                     start = get_character_index(
#                         source,
#                         statment.lineno,
#                         statment.col_offset
#                     )

#                     end = get_character_index(
#                         source,
#                         statment.end_lineno,
#                         statment.end_col_offset
#                     )

#                     statement_size = end - start

#                     # print(
#                     #     type(statment).__name__,
#                     #     "line:", statment.end_lineno,
#                     #     "end line:", statment.end_col_offset
#                     # )

#                     # print("Number of characters: ",
#                     #       last_character_index - first_character_index)

#                     # code = ast.get_source_segment(source, statment)
#                     # print("CODE:")
#                     # print(code)
#                     # print("Number of characters: ",
#                     #       last_character_index - first_character_index)
#                     print("\nSTATMENT:", type(statment).__name__)
#                     print("Start:", start)
#                     print("End:", end)
#                     print("Size:", end - start)
#                     # print(source[start:end + 1])
#                     print("-" * 90)

#                     if statement_size < 2000:
#                         all_chunks.append(
#                             MinimalSource(
#                                 file_path=str(file_path),
#                                 first_character_index=start,
#                                 last_character_index=end - 1,
#                             )
#                         )
#                         continue

#                     if hasattr(statment, "body"):

#                         # print("hello: ", type(child).__name__)

#                         for child in statment.body:

#                             start = get_character_index(
#                                 source,
#                                 child.lineno,
#                                 child.col_offset
#                             )

#                             end = get_character_index(
#                                 source,
#                                 child.end_lineno,
#                                 child.end_col_offset
#                             )

#                             print("\nCHILD:", type(child).__name__)
#                             print("Start:", start)
#                             print("End:", end)
#                             print("Size:", end - start)
#                             # print(source[start:end + 1])
#                             print("-" * 90)

#                             if end - start < 2000:
#                                 all_chunks.append(
#                                     MinimalSource(
#                                         file_path=str(file_path),
#                                         first_character_index=start,
#                                         last_character_index=end - 1,
#                                     )
#                                 )
#                                 continue
#                             if hasattr(child, "body"):
#                                 for child_of_child in child.body:

#                                     start = get_character_index(
#                                         source,
#                                         child_of_child.lineno,
#                                         child_of_child.col_offset
#                                     )

#                                     end = get_character_index(
#                                         source,
#                                         child_of_child.end_lineno,
#                                         child_of_child.end_col_offset
#                                     )

#                                     print("\nCHILD_OF_CHILD:", type(
#                                         child_of_child).__name__)
#                                     print("Start:", start)
#                                     print("End:", end)
#                                     print("Size:", end - start)
#                                     # print(source[start:end + 1])
#                                     print("-" * 90)

#                                     if end - start < 2000:
#                                         all_chunks.append(
#                                             MinimalSource(
#                                                 file_path=str(file_path),
#                                                 first_character_index=start,
#                                                 last_character_index=end - 1,
#                                             )
#                                         )
#                                         continue
#                                     if hasattr(child_of_child, "body"):
#                                         for petit_child in child_of_child.body:

#                                             start = get_character_index(
#                                                 source,
#                                                 petit_child.lineno,
#                                                 petit_child.col_offset
#                                             )

#                                             end = get_character_index(
#                                                 source,
#                                                 petit_child.end_lineno,
#                                                 petit_child.end_col_offset
#                                             )

#                                             print("\nCHILD_OF_CHILD:", type(
#                                                 petit_child).__name__)
#                                             print("Start:", start)
#                                             print("End:", end)
#                                             print("Size:", end - start)
#                                             # print(source[start:end + 1])
#                                             print("-" * 90)

#                                             if end - start < 2000:
#                                                 all_chunks.append(
#                                                     MinimalSource(
#                                                         file_path=str(file_path),
#                                                         first_character_index=start,
#                                                         last_character_index=end - 1,
#                                                     )
#                                                 )

#                     else:
#                         continue

#                 # break
#                 # continue
#                 # break

#                 # print("First Characters: ", first_character_index)
#                 # print("Last Characters: ", last_character_index)
#                 # print("Total Characters: ",
#                 #       last_character_index - first_character_index)
#                 # print("File Path: ", file_path)
#                 # return all_chunks

#     return all_chunks


# def main():
#     directory = Path("/goinfre/azebahad/RAG-against-the-machine")

#     chunks = python_chunker(directory, 20)

#     print("Python code chunks:\n", chunks)


# if __name__ == "__main__":
#     main()
