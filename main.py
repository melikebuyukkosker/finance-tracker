# main.py
import os
from db import init_db
from ui_main import start_app

# Veritabanı klasörü varsa oluştur
os.makedirs("database", exist_ok=True)

# Veritabanını başlat
init_db()

# Uygulamayı başlat
start_app()
