from pathlib import Path
from pydantic import BaseModel

class Chunk(BaseModel):
    content: str
    file_path: str
    first_character_index: int
    last_character_index: int

def chunk_text(text: str, max_size: int, path: Path) -> list[Chunk]:
    chunks: list[Chunk] = []

    for i in range(0, len(text), max_size):
        splited_text = text[i:i + max_size]
        first_character_index = i
        last_character_index = i + len(splited_text) - 1

        chunks.append(
                Chunk(
                    content=splited_text,
                    file_path=path.name,
                    first_character_index=first_character_index,
                    last_character_index=last_character_index)
                )

    return chunks

def index_directory(directory: Path) -> list[Chunk]:
    all_chunks: list[Chunk] = []
    for file_path in directory.glob("*.txt"):
        with file_path.open("r") as file:
            content = file.read()
        all_chunks.extend(chunk_text(content, 20, file_path))
    return all_chunks


def main():
    directory = Path(
        "../../RAG-against-the-machine/data/documents")
    chunks = index_directory(directory)
    print("Text to chinks: \n", chunks)


if __name__ == "__main__":
    main()

