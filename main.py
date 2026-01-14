import pandas as pd
import json

# ==========================================
# KONFIGURASI NAMA FILE
# ==========================================
# Ganti nama file ini sesuai nama file asli lu
input_file = 'Copy of 6000+ List Suplier Terlaris Shopee.xlsx' 
output_file = 'data_supplier.json'

# ==========================================
# 1. BACA FILE EXCEL
# ==========================================
print(f"Sedang membaca file {input_file}... Sabar ya Bro...")
# df = DataFrame (Tabel data di memori Python)
df = pd.read_excel(input_file)

# ==========================================
# 2. BERSIH-BERSIH & MAPPING (PENTING!)
# ==========================================
# Kita pilih kolom yg penting aja & ganti namanya biar enak dikoding di JS
# Format: 'Nama Kolom di Excel': 'Nama Baru di JSON'

kolom_yang_diambil = {
    'NamaProduk': 'nama',        # Ganti 'NamaProduk' sesuai header asli di Excel lu
    'Harga': 'harga_modal',
    'Kategori': 'kategori',
    'LinkToko': 'link_toko',
    'KotaPengiriman': 'kota',
    'JumlahTerjual': 'terjual'
}

# Cuma ambil kolom yg didaftarin di atas
df_clean = df[list(kolom_yang_diambil.keys())]

# Ganti nama kolomnya jadi versi JSON
df_clean = df_clean.rename(columns=kolom_yang_diambil)

# ==========================================
# 3. LOGIC TAMBAHAN (BIAR MAKIN CANGGIH)
# ==========================================
# Nambahin ID unik otomatis
df_clean['id'] = range(1, len(df_clean) + 1)

# Bikin Harga Jual Saran (Misal: Modal + 40%)
# .astype(int) biar gak ada koma desimal
df_clean['harga_jual_saran'] = (df_clean['harga_modal'] * 1.4).astype(int)

# Bikin kategori jadi huruf kecil semua & ganti spasi jadi underscore
# Biar gampang dicocokin (contoh: "Rumah Tangga" -> "rumah_tangga")
df_clean['kategori'] = df_clean['kategori'].str.lower().str.replace(' ', '_')

# ==========================================
# 4. EXPORT KE JSON
# ==========================================
print("Lagi convert ke JSON...")

# orient='records' bikin formatnya jadi [{...}, {...}] (List of Objects)
json_result = df_clean.to_json(orient='records', indent=2)

# Simpan ke file
with open(output_file, 'w') as f:
    f.write("const dataSupplier = " + json_result + ";")

print(f"✅ BERHASIL! File {output_file} sudah jadi. Tinggal sikat!")