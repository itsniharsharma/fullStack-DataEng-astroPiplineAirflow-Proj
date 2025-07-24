import json
import os

FILE_PATH = "data/rashiphal_db.json"

def load_rashiphal():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_rashiphal(data):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
