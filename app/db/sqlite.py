import sqlite3
from settings import DB_PATH

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

query = """
    CREATE TABLE IF NOT EXISTS activity_log (
        id integer PRIMARY KEY,
        status text NOT NULL,
        action text NOT NULL,
        ip_address text NOT NULL,
        user text NOT NULL,
        created_at datetime NOT NULL
    );
"""

cursor.execute(query)
conn.commit()
