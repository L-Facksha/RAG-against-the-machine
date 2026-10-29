from pathlib import Path
from src.chunking.chuncker import Chunk, python_chunker, markdown_chunker


def python_indexer(path: Path, max_size) -> list[Chunk]:
    all_chunks: list[Chunk] = []

    for path_file in path.rglob("*"):
        if path_file.suffix == ".py":
            all_chunks.extend(python_chunker(path_file, max_size))
        elif path_file.suffix == ".md":
            all_chunks.extend(markdown_chunker(path_file, max_size))
        else:
            continue

    return all_chunks


# def main():
#     repo_root = Path.cwd()  # Get the root directory of the project
#     # print(repo_root)
#     directory = repo_root / "data" / "raw"  # Specify the directory to index
#     # print(directory)
#     chunks = python_indexer(directory, 2000)
#     print(chunks)
#     print(f"all {len(chunks)} offsets verified correct")


# if __name__ == "__main__":
#     main()
