# ⚙️ Automated Crypto ETL Pipeline (Data Engineering Project)

![ETL Status]
<img width="765" height="217" alt="Screenshot 2026-03-08 at 19 36 00" src="https://github.com/user-attachments/assets/3ff402be-ece5-4697-a0a9-0b4b29e61c45" />

![MySQL]
<img width="977" height="697" alt="Screenshot 2026-03-08 at 19 36 29" src="https://github.com/user-attachments/assets/1cd688e0-cb22-45a5-9686-5f8be515c0e2" />

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

*(Hapus baris ini dan masukkan screenshot terminal lu yang lagi jalan otomatis di sini)*

*(Hapus baris ini dan masukkan screenshot tabel DBeaver lu yang datanya udah masuk di sini)*

---
**👨‍💻 Author:** Wisma Jaya Laksana | Calon Data Engineer
