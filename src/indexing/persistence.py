from src.indexing.vectorizer import vectorize_data
from pathlib import Path
import joblib


def save_index(directory: str, max_size: int):
    tf_idf, vectorizer, chunks = vectorize_data(directory, max_size)
    index = {
        'tf_idf': tf_idf,
        'vectorizer': vectorizer,
        'chunks': chunks
    }
    processed_dir = Path('data/processed')
    processed_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(index, processed_dir / 'index.joblib')
    c = joblib.load("data/processed/index.joblib")
    # print(len(c['chunks']))
    # print(c['chunks'])


def main():
    repo_root = Path.cwd()
    # print(repo_root)
    directory = repo_root / "data" / "raw"
    # print(directory)
    save_index(directory, 2000)
    # print("hello")
    # print(len(recovred_data) == len(chunk))
    # print(recovred_data)


if __name__ == "__main__":
    main()
