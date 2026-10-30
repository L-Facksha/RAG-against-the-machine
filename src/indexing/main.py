from src.indexing.preparation import preparation_data
from pathlib import Path


def main():
    repo_root = Path.cwd()
    # print(repo_root)
    directory = repo_root / "data" / "raw"
    # print(directory)
    recovred_data, chunk = preparation_data(directory, 2000)
    # print("hello")
    print(len(recovred_data) == len(chunk))
    # print(recovred_data)


if __name__ == "__main__":
    main()
