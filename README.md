# ⚙️ Automated Crypto ETL Pipeline (Data Engineering Project)

![ETL Status](https://img.shields.io/badge/Status-Completed-success) ![Python](https://img.shields.io/badge/Python-3.x-blue) ![MySQL](https://img.shields.io/badge/MySQL-Local-orange)

## 📝 Project Overview
Proyek ini adalah sebuah **End-to-End ETL (Extract, Transform, Load) Pipeline** otomatis yang dirancang untuk menarik data pasar *Cryptocurrency* secara *real-time*, membersihkannya, dan menyimpannya ke dalam Relational Database (MySQL) untuk keperluan analisis historis. 

Proyek ini dibuat untuk mensimulasikan tugas inti harian seorang **Data Engineer**, dari penarikan data mentah via API hingga penyimpanan data *time-series* yang siap digunakan oleh tim *Data Science / Data Analytics*.

---

## 🏗️ Pipeline Architecture (Arsitektur E-T-L)

1. **🎣 EXTRACT (Penarikan Data):** Mengambil data Top 10 Cryptocurrency (berdasarkan Market Cap) secara *live* dari **CoinGecko Public API** menggunakan metode *HTTP GET request* (`requests` library).
   
2. **🧹 TRANSFORM (Pembersihan Data):** Memproses data JSON mentah menggunakan **Pandas DataFrame**. Tahapan ini mencakup:
   * Seleksi kolom esensial (ID, Symbol, Name, Price, Market Cap).
   * Penyesuaian nama kolom agar *match* 100% dengan skema *database* target.
   * Pembersihan zona waktu (*timezone parsing*) menggunakan `datetime`.

3. **🚚 LOAD (Penyimpanan Data):** Mengirim data yang sudah bersih ke tabel `crypto_prices` di dalam **MySQL Database**. Menggunakan metode `append` melalui `SQLAlchemy` untuk menumpuk data secara historis (*Time-Series Logging*).

---

## 🛠️ Tech Stack & Tools
* **Language:** Python 
* **Libraries:** `requests`, `pandas`, `SQLAlchemy`, `pymysql`, `python-dotenv`
* **Database:** MySQL (DBeaver for Database Management)
* **Data Source:** CoinGecko API

---

## 🤖 Key Features
* **Continuous Automation:** Pipeline ini dilengkapi dengan skrip otomatisasi sederhana (`while True` dan `time.sleep`) untuk menarik data secara berkala setiap menit layaknya *Cron Job/Airflow* skala kecil.
* **Security Best Practices:** Mengimplementasikan keamanan standar industri menggunakan *Environment Variables* (`.env`) dan `.gitignore` untuk mencegah kebocoran *database connection string* dan kredensial ke publik.

---

## 📸 Preview Hasil (Terminal & Database)

<img width="1079" height="405" alt="Screenshot 2026-03-09 at 17 28 32" src="https://github.com/user-attachments/assets/7a6f87ee-84a8-40c1-89af-2fdf285b8b9b" />


<img width="977" height="697" alt="Screenshot 2026-03-08 at 19 36 29" src="https://github.com/user-attachments/assets/daabaff1-effb-445a-9f12-25b081d383d5" />

---
**Author:** Wisma Jaya Laksana
