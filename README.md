# Finance Tracker (Kişisel Finans Takip Sistemi)

Bu proje, kişisel finans yönetimini kolaylaştırmak için geliştirilmiş bir Python tabanlı bir uygulamadır. Kullanıcılar gelir ve giderlerini kaydedebilir, grafiklerle harcama analizleri yapabilir, belirli bir kategoriye göre filtreleme yapabilir ve harcama sınırı belirleyerek uyarı alabilirler. Ayrıca, harcamalar hakkında PDF raporları oluşturabilir ve verilerini CSV formatında yedekleyip içe aktarabilirler.

## Özellikler
- Gelir ve gider takibi
- Grafik analizleri (pasta grafiği, zaman bazlı çizgi grafiği)
- Kategori bazlı harcama takibi
- Harcama sınırı belirleme ve uyarı
- Yedekleme ve içe aktarma (CSV)
- PDF rapor üretme

## Kurulum
1. GitHub reposundan projeyi klonlayın:
    ```bash
    git clone https://github.com/kullanici_adiniz/finance-tracker.git
    ```
2. Sanal ortam oluşturun ve gerekli bağımlılıkları yükleyin:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3. Uygulamayı başlatın:
    ```bash
    python main.py
    ```

## Teknolojiler
- Python
- Tkinter (GUI)
- SQLite (Veritabanı)
- Matplotlib (Grafik Analizi)
- ReportLab (PDF Raporu)
