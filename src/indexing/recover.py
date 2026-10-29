from pathlib import Path


def recover_data(path: Path, first_index: int, last_index: int) -> str:
    repo_root = Path(__file__).resolve().parents[2]
    absolute_path = repo_root / path
    with open(absolute_path, "r", encoding="utf-8"):
        source = absolute_path.read_text(encoding="utf-8")
    return source[first_index:last_index + 1]
