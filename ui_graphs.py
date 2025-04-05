# ui_graphs.py
import tkinter as tk
import sqlite3
import matplotlib.pyplot as plt
from tkinter import ttk
from collections import defaultdict
from datetime import datetime

def open_graphs_window():
    window = tk.Toplevel()
    window.title("Grafik Analizi")
    window.geometry("300x200")

    ttk.Button(window, text="Kategori Bazlı Harcama (Pasta Grafik)", command=draw_pie_chart).pack(pady=10)
    ttk.Button(window, text="Zaman Bazlı Harcama (Çizgi Grafik)", command=draw_time_chart).pack(pady=10)

def draw_pie_chart():
    conn = sqlite3.connect("database/finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE type = 'expense' GROUP BY category")
    data = cursor.fetchall()
    conn.close()

    if not data:
        print("Gösterilecek veri yok.")
        return

    labels = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Kategori Bazlı Harcama Dağılımı")
    plt.tight_layout()
    plt.show()

def draw_time_chart():
    conn = sqlite3.connect("database/finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT date, SUM(amount) FROM transactions WHERE type = 'expense' GROUP BY date ORDER BY date")
    data = cursor.fetchall()
    conn.close()

    if not data:
        print("Gösterilecek veri yok.")
        return

    dates = [datetime.strptime(row[0], "%Y-%m-%d") for row in data]
    amounts = [row[1] for row in data]

    plt.figure(figsize=(8, 4))
    plt.plot(dates, amounts, marker='o', linestyle='-')
    plt.title("Zaman Bazlı Harcamalar")
    plt.xlabel("Tarih")
    plt.ylabel("Tutar")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
