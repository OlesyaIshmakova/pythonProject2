import os.path

FILES_DIR = os.path.dirname(__file__)

def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)

CSV_F_PATH = get_path(filename="books.csv")
JSON_F_PATH = get_path(filename="users.json")