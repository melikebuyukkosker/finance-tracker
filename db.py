# db.py
import sqlite3

def init_db():
    conn = sqlite3.connect('database/finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT CHECK(type IN ('income', 'expense')) NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_transaction(tx_type, amount, category, date, description):
    conn = sqlite3.connect('database/finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (type, amount, category, date, description)
        VALUES (?, ?, ?, ?, ?)
    ''', (tx_type, amount, category, date, description))
    conn.commit()
    conn.close()
