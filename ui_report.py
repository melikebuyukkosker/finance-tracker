# ui_report.py
import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import sqlite3

def generate_pdf_report():
    conn = sqlite3.connect("database/finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        messagebox.showerror("Hata", "Veritabanında rapor için veri yok.")
        return

    pdf_file = "finance_report.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.drawString(100, 750, "Gelir-Gider Raporu")

    y_position = 730
    for row in rows:
        c.drawString(100, y_position, f"ID: {row[0]}, Tip: {row[1]}, Miktar: {row[2]}, Kategori: {row[3]}, Tarih: {row[4]}, Açıklama: {row[5]}")
        y_position -= 20
        if y_position < 100:
            c.showPage()
            y_position = 750

    c.save()
    messagebox.showinfo("Başarılı", f"Rapor başarıyla oluşturuldu: {pdf_file}")
