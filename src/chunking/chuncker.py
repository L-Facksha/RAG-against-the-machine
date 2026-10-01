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
#     statments = ['If', 'For', 'While', 'Def']

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
#                 if last_character_index - first_character_index >= 2000:
#                     for statment in node.body:
#                         print(first_character_index)
#                         print(last_character_index)
#                         print(hasattr(statment, "body"))
#                         if hasattr(statment, "body"):
#                             first_character_index = get_character_index(
#                                 source,
#                                 statment.lineno,
#                                 statment.col_offset
#                             )
#                             end_character_index = get_character_index(
#                                 source, statment.end_lineno, statment.end_col_offset)
#                             last_character_index = end_character_index - 1
#                             # print("Number of characters: ",
#                             #       last_character_index - first_character_index)
#                             print(
#                                 type(statment).__name__,
#                                 "line:", statment.end_lineno,
#                                 "end line:", statment.end_col_offset
#                             )
#                             # code = ast.get_source_segment(source, statment)
#                             # print("CODE:")
#                             # print(code)
#                             # print("Number of characters: ",
#                             #       last_character_index - first_character_index)

#                             if last_character_index - first_character_index >= 2000:
#                                 # print("hello: ", type(child).__name__)
#                                 for child in statment.body:

#                                     start = get_character_index(
#                                         source,
#                                         child.lineno,
#                                         child.col_offset
#                                     )

#                                     end = get_character_index(
#                                         source,
#                                         child.end_lineno,
#                                         child.end_col_offset
#                                     )

#                                     last_character_index = end - 1

#                                     if last_character_index - first_character_index >= 2000:
#                                         break

#                                     print("\nSTATEMENT:", type(child).__name__)
#                                     print("Start:", start)
#                                     print("End:", end)
#                                     print("Size:", end - start)
#                                     print(ast.get_source_segment(
#                                         source, child))

#                             # if last_character_index - first_character_index >= 2000:
#                             #     print(first_character_index)
#                             #     print(last_character_index)
#                             #     print(file_path)
#                             #     print("lalala")
#                             #     return all_chunks
#                         else:
#                             continue
#                         # break
#                     # continue
#                     # break

#                     # print("First Characters: ", first_character_index)
#                     # print("Last Characters: ", last_character_index)
#                     # print("Total Characters: ",
#                     #       last_character_index - first_character_index)
#                     # print("File Path: ", file_path)
#                     # return all_chunks

#                 all_chunks.append(
#                     MinimalSource(
#                         file_path=str(file_path),
#                         first_character_index=first_character_index,
#                         last_character_index=last_character_index,
#                     )
#                 )

#     return all_chunks


# def main():
#     directory = Path("/goinfre/azebahad/RAG-against-the-machine")

#     chunks = python_chunker(directory, 20)

#     print("Python code chunks:\n", chunks)


# if __name__ == "__main__":
#     main()


from pathlib import Path

import ast

from src.models.models import MinimalSource


# def split_large_node(source, node, max_size):
#     tree = ast.parse(source)
#     for node in ast.walk(tree):
#         if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
#             first_character_index = get_character_index(
#                 source,
#                 node.lineno,
#                 node.col_offset
#             )
#             end_character_index = get_character_index(
#                 source,
#                 node.end_lineno,
#                 node.end_col_offset
#             )


def get_character_index(source: str, line: int, column: int) -> int:
    lines = source.splitlines(keepends=True)
    # print(lines)

    return sum(len(current_line) for current_line in lines[:line - 1]) + column


def python_chunker(path: Path, max_size: int) -> list[MinimalSource]:
    all_chunks: list[MinimalSource] = []

    print(path)

    for file_path in path.glob("**/*.py"):
        with open(file_path, "r") as f:
            source = f.read()

        try:
            tree = ast.parse(source)
        except SyntaxError:
            continue

        for node in ast.walk(tree):

            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):

                first_character_index = get_character_index(
                    source,
                    node.lineno,
                    node.col_offset
                )

                end_character_index = get_character_index(
                    source,
                    node.end_lineno,
                    node.end_col_offset
                )

                last_character_index = end_character_index - 1

                # node is small enough
                if last_character_index - first_character_index < 2000:
                    all_chunks.append(
                        MinimalSource(
                            file_path=str(file_path),
                            first_character_index=first_character_index,
                            last_character_index=last_character_index,
                        )
                    )
                    continue

                # node is too large
                for statment in node.body:

                    # print(first_character_index)
                    # print(last_character_index)
                    # print(hasattr(statment, "body"))

                    start = get_character_index(
                        source,
                        statment.lineno,
                        statment.col_offset
                    )

                    end = get_character_index(
                        source,
                        statment.end_lineno,
                        statment.end_col_offset
                    )

                    statement_size = end - start

                    # print(
                    #     type(statment).__name__,
                    #     "line:", statment.end_lineno,
                    #     "end line:", statment.end_col_offset
                    # )

                    # print("Number of characters: ",
                    #       last_character_index - first_character_index)

                    # code = ast.get_source_segment(source, statment)
                    # print("CODE:")
                    # print(code)
                    # print("Number of characters: ",
                    #       last_character_index - first_character_index)
                    print("\nSTATMENT:", type(statment).__name__)
                    print("Start:", start)
                    print("End:", end)
                    print("Size:", end - start)
                    # print(source[start:end + 1])
                    print("-" * 90)

                    if statement_size < 2000:
                        all_chunks.append(
                            MinimalSource(
                                file_path=str(file_path),
                                first_character_index=start,
                                last_character_index=end - 1,
                            )
                        )
                        continue

                    if hasattr(statment, "body"):

                        # print("hello: ", type(child).__name__)

                        for child in statment.body:

                            start = get_character_index(
                                source,
                                child.lineno,
                                child.col_offset
                            )

                            end = get_character_index(
                                source,
                                child.end_lineno,
                                child.end_col_offset
                            )

                            print("\nCHILD:", type(child).__name__)
                            print("Start:", start)
                            print("End:", end)
                            print("Size:", end - start)
                            # print(source[start:end + 1])
                            print("-" * 90)

                            if end - start < 2000:
                                all_chunks.append(
                                    MinimalSource(
                                        file_path=str(file_path),
                                        first_character_index=start,
                                        last_character_index=end - 1,
                                    )
                                )
                                continue
                            if hasattr(child, "body"):
                                for child_of_child in child.body:

                                    start = get_character_index(
                                        source,
                                        child_of_child.lineno,
                                        child_of_child.col_offset
                                    )

                                    end = get_character_index(
                                        source,
                                        child_of_child.end_lineno,
                                        child_of_child.end_col_offset
                                    )

                                    print("\nCHILD_OF_CHILD:", type(
                                        child_of_child).__name__)
                                    print("Start:", start)
                                    print("End:", end)
                                    print("Size:", end - start)
                                    # print(source[start:end + 1])
                                    print("-" * 90)

                                    if end - start < 2000:
                                        all_chunks.append(
                                            MinimalSource(
                                                file_path=str(file_path),
                                                first_character_index=start,
                                                last_character_index=end - 1,
                                            )
                                        )
                                        continue
                                    if hasattr(child_of_child, "body"):
                                        for petit_child in child_of_child.body:

                                            start = get_character_index(
                                                source,
                                                petit_child.lineno,
                                                petit_child.col_offset
                                            )

                                            end = get_character_index(
                                                source,
                                                petit_child.end_lineno,
                                                petit_child.end_col_offset
                                            )

                                            print("\nCHILD_OF_CHILD:", type(
                                                petit_child).__name__)
                                            print("Start:", start)
                                            print("End:", end)
                                            print("Size:", end - start)
                                            # print(source[start:end + 1])
                                            print("-" * 90)

                                            if end - start < 2000:
                                                all_chunks.append(
                                                    MinimalSource(
                                                        file_path=str(file_path),
                                                        first_character_index=start,
                                                        last_character_index=end - 1,
                                                    )
                                                )

                    else:
                        continue

                # break
                # continue
                # break

                # print("First Characters: ", first_character_index)
                # print("Last Characters: ", last_character_index)
                # print("Total Characters: ",
                #       last_character_index - first_character_index)
                # print("File Path: ", file_path)
                # return all_chunks

    return all_chunks


def main():
    directory = Path("/goinfre/azebahad/RAG-against-the-machine")

    chunks = python_chunker(directory, 20)

    print("Python code chunks:\n", chunks)


if __name__ == "__main__":
    main()
