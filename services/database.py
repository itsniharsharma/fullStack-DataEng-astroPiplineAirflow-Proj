import sqlite3
import os

DB_PATH = os.path.join("data", "dataflow.db")

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rashiphal (
            sign TEXT PRIMARY KEY,
            content TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(data: dict):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for sign, content in data.items():
        cursor.execute('''
            INSERT INTO rashiphal (sign, content)
            VALUES (?, ?)
            ON CONFLICT(sign) DO UPDATE SET content=excluded.content
        ''', (sign, content))
    conn.commit()
    conn.close()
