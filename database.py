import sqlite3

conn = sqlite3.connect("goldmind.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    telegram_id INTEGER PRIMARY KEY,
    username TEXT,
    points INTEGER DEFAULT 0,
    streak INTEGER DEFAULT 0,
    plan TEXT DEFAULT 'free'
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER,
    direction TEXT,
    price_open REAL,
    timeframe INTEGER,
    timestamp INTEGER,
    resolved INTEGER DEFAULT 0
)
""")

conn.commit()
