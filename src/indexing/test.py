from src.indexing.indexer import python_indexer
from src.indexing.recover import recover_data
from src.chunking.chuncker import Chunk
from pathlib import Path


def main():
    chunks: list[Chunk]
    repo_root = Path.cwd()  # Get the root directory of the project
    # print(repo_root)
    directory = repo_root / "data" / "raw"  # Specify the directory to index
    # print(directory)
    chunks = python_indexer(directory, 2000)
    for c in chunks:
        data = recover_data(
            c.file_path, c.first_character_index, c.last_character_index)
        print(data)
        print(c.first_character_index)
        print(c.last_character_index)
        break
    # print(f"all {len(chunks)} offsets verified correct")


if __name__ == "__main__":
    main()
