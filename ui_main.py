# ui_main.py
import tkinter as tk
from ui_form import open_form
from ui_list import open_list_window
from ui_graphs import open_graphs_window
from ui_limits import open_limits_window
from ui_backup import open_backup_window
from ui_report import generate_pdf_report

def start_app():
    root = tk.Tk()
    root.title("Kişisel Finans Takip Sistemi")
    root.geometry("400x200")

    tk.Label(root, text="Finans Takip Paneli", font=("Arial", 16)).pack(pady=20)

    tk.Button(root, text="Gelir/Gider Ekle", command=open_form, width=20).pack(pady=5)

    tk.Button(root, text="Kayıtları Listele", command=open_list_window, width=20).pack(pady=5)

    tk.Button(root, text="Grafik Analizi", command=open_graphs_window, width=20).pack(pady=5)

    tk.Button(root, text="Harcama Sınırı", command=open_limits_window, width=20).pack(pady=5)

    tk.Button(root, text="Yedekleme ve İçe Aktarma", command=open_backup_window, width=20).pack(pady=5)

    tk.Button(root, text="PDF Raporu Oluştur", command=generate_pdf_report, width=20).pack(pady=5)

    root.mainloop()
