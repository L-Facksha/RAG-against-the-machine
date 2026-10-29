from src.indexing.recover import recover_data
from src.indexing.indexer import python_indexer
from src.chunking.chuncker import Chunk
from pathlib import Path


def preparation_data() -> tuple[list[str], list[Chunk]]:
    chunks: list[Chunk]
    repo_root = Path.cwd()
    # print(repo_root)
    directory = repo_root / "data" / "raw"
    # print(directory)
    chunks = python_indexer(directory, 2000)
    recovred_data: list[str] = []
    for c in chunks:
        data = recover_data(
            c.file_path, c.first_character_index, c.last_character_index)
        recovred_data.append(data)
    return recovred_data, chunks
