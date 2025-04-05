# ui_limits.py
import tkinter as tk
from tkinter import messagebox
import sqlite3

def open_limits_window():
    window = tk.Toplevel()
    window.title("Harcama Sınırı Belirleme")
    window.geometry("400x200")

    # Harcama sınırı girişi
    tk.Label(window, text="Aylık Harcama Limiti (TL):").pack(pady=10)
    limit_entry = tk.Entry(window)
    limit_entry.pack(pady=5)

    def check_expenses():
        limit = limit_entry.get()
        if not limit.isdigit():
            messagebox.showerror("Hata", "Geçersiz sınır. Lütfen bir sayı girin.")
            return

        limit = float(limit)
        conn = sqlite3.connect("database/finance.db")
        cursor = conn.cursor()

        # Aylık toplam harcama
        cursor.execute("SELECT SUM(amount) FROM transactions WHERE type = 'expense' AND strftime('%Y-%m', date) = strftime('%Y-%m', 'now')")
        total_expenses = cursor.fetchone()[0] or 0
        conn.close()

        if total_expenses > limit:
            messagebox.showwarning("Dikkat", f"Bu ayki harcamanız {total_expenses} TL ve sınırınızı {limit} TL aşmış!")
        else:
            messagebox.showinfo("Durum", f"Bu ayki harcamanız {total_expenses} TL, sınırınızı aşmadınız.")

    ttk.Button(window, text="Harcama Durumunu Kontrol Et", command=check_expenses).pack(pady=10)
