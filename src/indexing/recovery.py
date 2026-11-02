from pathlib import Path
import joblib


def load_index() -> dict:
    pth = Path('data/processed/index.joblib')
    try:
        return joblib.load(pth)
    except FileNotFoundError:
        print("ERROR: You should build the vocabulary first (indexing)")
        return None
