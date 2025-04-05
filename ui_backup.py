# ui_backup.py
import tkinter as tk
from tkinter import filedialog
import sqlite3
import csv

def backup_data():
    conn = sqlite3.connect("database/finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()

    # CSV'ye yedekleme
    with open("backup_transactions.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([desc[0] for desc in cursor.description])  # Başlıklar
        writer.writerows(rows)

    conn.close()
    print("Veriler yedeklendi: backup_transactions.csv")

def import_data():
    file_path = filedialog.askopenfilename(title="CSV Dosyası Seç", filetypes=[("CSV Files", "*.csv")])
    if not file_path:
        return

    with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        headers = next(reader)  # İlk satır başlıkları al
        rows = [row for row in reader]

    conn = sqlite3.connect("database/finance.db")
    cursor = conn.cursor()

    for row in rows:
        cursor.execute("INSERT INTO transactions (type, amount, category, date, description) VALUES (?, ?, ?, ?, ?)", row)
    
    conn.commit()
    conn.close()
    print("Veriler içe aktarıldı.")

def open_backup_window():
    window = tk.Toplevel()
    window.title("Yedekleme ve İçe Aktarma")
    window.geometry("400x200")

    ttk.Button(window, text="Verileri Yedekle", command=backup_data).pack(pady=10)
    ttk.Button(window, text="CSV'den İçe Aktar", command=import_data).pack(pady=10)
