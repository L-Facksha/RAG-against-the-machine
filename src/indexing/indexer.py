from pathlib import Path
from src.chunking.chuncker import Chunk, python_chunker, markdown_chunker


def python_indexer(path: Path, max_size) -> list[Chunk]:
    all_chunks: list[Chunk] = []

    for path_file in path.glob("*"):
        if path_file.suffix(".py"):
            all_chunks.extend(python_chunker(path_file, max_size))
        elif path_file.suffix(".md"):
            all_chunks.append(markdown_chunker(path_file, max_size))
        else:
            continue

    return all_chunks
