from pathlib import Path
import ast

from src.models.models import MinimalSource


def get_character_index(source: str, line: int, column: int) -> int:
    lines = source.splitlines(keepends=True)
    print(lines)

    return sum(len(current_line) for current_line in lines[:line - 1]) + column


def python_chunker(path: Path, max_size: int) -> list[MinimalSource]:
    all_chunks: list[MinimalSource] = []

    for file_path in path.glob("**/*.py"):
        # print(file_path)
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
                if last_character_index - first_character_index >= 2000:
                    print("First Characters: ", first_character_index)
                    print("Last Characters: ", last_character_index)
                    print("Total Characters: ",
                          last_character_index - first_character_index)
                    print("File Path: ", file_path)
                    return all_chunks

                all_chunks.append(
                    MinimalSource(
                        file_path=str(file_path),
                        first_character_index=first_character_index,
                        last_character_index=last_character_index,
                    )
                )

    return all_chunks


def main():
    directory = Path("/goinfre/azebahad/RAG-against-the-machine")

    chunks = python_chunker(directory, 20)

    print("Python code chunks:\n", chunks)


if __name__ == "__main__":
    main()
