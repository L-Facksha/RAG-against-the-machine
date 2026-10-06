from pathlib import Path
from src.chunking.chuncker import Chunk, python_chunker

def python_indexer(path: Path, max_size) -> list[Chunk]:
    all_chunks: list[Chunk] = []
    
    for path_file in path.glob("*"):
        if path_file.suffix(".py"):
            all_chunks.extend(python_chunker(path_file, 100))
        elif path_file.suffix(".md"):
            