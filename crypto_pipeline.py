import requests
import pandas as pd
import time
from sqlalchemy import create_engine
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def run_crypto_etl():
    print("🚀 Memulai proses ETL Pipeline...")

    #proses extract
    print("⏳ [EXTRACT] Menarik data live dari CoinGecko API...")
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,  # Kita ambil Top 10 Koin (Bitcoin, Ethereum, dll)
        "page": 1,
        "sparkline": "false"
    }
    
    response = requests.get(url, params=params, timeout=10)
    
    if response.status_code != 200:
        print("❌ Gagal menarik data! Coba lagi nanti.")
        return
    
    raw_data = response.json()
    print("✅ [EXTRACT] Data berhasil ditarik!")

    #transform (proses bersih-bersih data)
    print("⏳ [TRANSFORM] Merapikan data dengan Pandas...")
    df = pd.DataFrame(raw_data)
    
    # Pilih kolom yang dibutuhkan saja
    df = df[['id', 'symbol', 'name', 'current_price', 'market_cap', 'last_updated']]
    
    # Ganti nama kolom supaya sama persis sama kolom table di mySQL
    df.rename(columns={
        'id': 'coin_id',
        'name': 'coin_name',
        'current_price': 'current_price_usd',
        'market_cap': 'market_cap_usd'
    }, inplace=True)
    
    # rapikan format waktu (buang zona waktu biar MySQL nggak bingung)
    df['last_updated'] = pd.to_datetime(df['last_updated']).dt.tz_localize(None)
    
    print("✅ [TRANSFORM] Data bersih dan siap dikirim!")

    #load (simpan data ke mySQL)
    print("⏳ [LOAD] Menghubungkan ke Database MySQL...")
    
    db_connection_str = os.getenv("DB_CONNECTION")
    
    try:
        engine = create_engine(db_connection_str)
        # Tembak data ke tabel 'crypto_prices'
        df.to_sql(name='crypto_prices', con=engine, if_exists='append', index=False)
        print("✅ [LOAD] Sukses! 10 Data Kripto terbaru berhasil masuk ke MySQL! 🎉")
    except Exception as e:
        print(f"❌ [LOAD] Gagal masukin ke database: {e}")

# Jalankan fungsi utamanya
if __name__ == "__main__":
    run_crypto_etl()

#atau

# Jalankan fungsi utamanya secara OTOMATIS
if __name__ == "__main__":
    print("🤖 Robot ETL Kripto Diaktifkan!")
    
    # Looping tanpa batas (while True) biar dia jalan terus
    while True:
        run_crypto_etl()
        
        # Suruh robotnya tidur 60 detik (1 menit) sebelum kerja lagi
        print("⏳ Robot sedang tidur... Menunggu 1 menit untuk tarikan data selanjutnya...\n")
        time.sleep(60)    