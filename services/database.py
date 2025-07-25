import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'rashiphal.db')

def init_db():
    """Create the rashiphal table if it doesn't exist"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rashiphal (
            sign TEXT PRIMARY KEY,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(sign, content):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO rashiphal (sign, content)
        VALUES (?, ?)
        ON CONFLICT(sign) DO UPDATE SET content=excluded.content
    ''', (sign, content))
    conn.commit()
    conn.close()

def load_from_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT sign, content FROM rashiphal')
    rows = cursor.fetchall()
    conn.close()
    return {sign: content for sign, content in rows}
