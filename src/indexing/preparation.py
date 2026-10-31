from src.indexing.recover import recover_data
from src.indexing.indexer import python_indexer
from src.chunking.chuncker import Chunk


def preparation_data(directory: str, max_size: int) -> tuple[
    list[str], list[Chunk]
]:
    chunks: list[Chunk]
    chunks = python_indexer(directory, max_size)
    recovred_data: list[str] = []
    for c in chunks:
        data = recover_data(
            c.file_path, c.first_character_index, c.last_character_index)
        recovred_data.append(data)
    return recovred_data, chunks
