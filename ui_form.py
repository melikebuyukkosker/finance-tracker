# ui_form.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from db import insert_transaction
from datetime import date

def open_form():
    window = tk.Toplevel()
    window.title("Gelir/Gider Ekle")
    window.geometry("300x350")

    tk.Label(window, text="İşlem Türü:").pack(pady=5)
    tx_type = tk.StringVar(value="expense")
    ttk.Radiobutton(window, text="Gider", variable=tx_type, value="expense").pack()
    ttk.Radiobutton(window, text="Gelir", variable=tx_type, value="income").pack()

    tk.Label(window, text="Tutar:").pack()
    amount_entry = ttk.Entry(window)
    amount_entry.pack()

    tk.Label(window, text="Kategori:").pack()
    category_entry = ttk.Entry(window)
    category_entry.pack()

    tk.Label(window, text="Tarih (YYYY-MM-DD):").pack()
    date_entry = ttk.Entry(window)
    date_entry.insert(0, str(date.today()))
    date_entry.pack()

    tk.Label(window, text="Açıklama:").pack()
    desc_entry = ttk.Entry(window)
    desc_entry.pack()

    def submit():
        try:
            amount = float(amount_entry.get())
            insert_transaction(
                tx_type.get(),
                amount,
                category_entry.get(),
                date_entry.get(),
                desc_entry.get()
            )
            messagebox.showinfo("Başarılı", "İşlem kaydedildi!")
            window.destroy()
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu:\n{e}")

    ttk.Button(window, text="Kaydet", command=submit).pack(pady=10)
