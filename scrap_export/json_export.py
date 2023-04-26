import pandas as pd
import sqlite3

# Baca file JSON dan ubah menjadi dataframe
df = pd.read_json('scrap_export/categorized_data.json')

# Buka koneksi ke database SQLite
conn = sqlite3.connect('minimarket.db')

# Simpan dataframe ke database SQLite
df.to_sql('barang', conn, if_exists='append', index=False)

# Tutup koneksi
conn.close()