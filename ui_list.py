# ui_list.py
import tkinter as tk
from tkinter import ttk
import sqlite3

def open_list_window():
    window = tk.Toplevel()
    window.title("Geçmiş Harcamalar")
    window.geometry("700x400")

    # Filtre alanları
    filter_frame = ttk.Frame(window)
    filter_frame.pack(pady=10)

    tk.Label(filter_frame, text="Kategori:").grid(row=0, column=0, padx=5)
    category_entry = ttk.Entry(filter_frame)
    category_entry.grid(row=0, column=1, padx=5)

    tk.Label(filter_frame, text="Başlangıç Tarihi (YYYY-MM-DD):").grid(row=0, column=2, padx=5)
    start_date_entry = ttk.Entry(filter_frame)
    start_date_entry.grid(row=0, column=3, padx=5)

    tk.Label(filter_frame, text="Bitiş Tarihi (YYYY-MM-DD):").grid(row=0, column=4, padx=5)
    end_date_entry = ttk.Entry(filter_frame)
    end_date_entry.grid(row=0, column=5, padx=5)

    # Treeview tablo
    columns = ("id", "type", "amount", "category", "date", "description")
    tree = ttk.Treeview(window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col.capitalize())
    tree.pack(fill="both", expand=True)

    def load_data():
        for i in tree.get_children():
            tree.delete(i)

        conn = sqlite3.connect("database/finance.db")
        cursor = conn.cursor()

        query = "SELECT * FROM transactions WHERE 1=1"
        params = []

        category = category_entry.get().strip()
        if category:
            query += " AND category LIKE ?"
            params.append(f"%{category}%")

        start_date = start_date_entry.get().strip()
        if start_date:
            query += " AND date >= ?"
            params.append(start_date)

        end_date = end_date_entry.get().strip()
        if end_date:
            query += " AND date <= ?"
            params.append(end_date)

        cursor.execute(query, params)
        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", "end", values=row)

        conn.close()

    ttk.Button(window, text="Filtrele", command=load_data).pack(pady=5)

    load_data()  # Başlangıçta tüm verileri getir
