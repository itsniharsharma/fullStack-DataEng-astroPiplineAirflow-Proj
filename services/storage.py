import json
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'rashiphal.json')

def load_rashiphal():
    try:
        if not os.path.exists(FILE_PATH):
            return {}
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading rashiphal: {e}")
        return {}

def save_rashiphal(data):
    try:
        os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving rashiphal: {e}")
