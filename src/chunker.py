from pathlib import Path


def chunk_text(text: str, max_size: int) -> list[dict]:
    chunks: list[dict] = []
    for i in range(0, len(text), max_size):
        splited_text = text[i:i + max_size]
        first_character_index = i
        last_character_index = i + len(splited_text) - 1
        chunks.append({"content": splited_text,
                       "first_character_index": first_character_index,
                       "last_character_index": last_character_index})
    return chunks


def main():
    f_path = Path(
        "../../RAG-against-the-machine/data/documents/linux.txt")
    with f_path.open("r") as file:
        data = file.read()
    chunks = chunk_text(data, 5)
    print("Text to chinks: \n", chunks)


if __name__ == "__main__":
    main()
