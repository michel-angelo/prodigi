import cv2
import os
import shutil

# === KONFIGURASI FOLDER ===
source_folder = "mentahan"  # Folder tempat video numpuk
folders = {
    ord("1"): "Kategori_Fashion",
    ord("2"): "Kategori_RumahTangga",
    ord("3"): "Kategori_Elektronik",
    ord("4"): "Kategori_Kesehatan",
    ord("s"): "Sampah_Skip",  # Buat video gak jelas
}

# Bikin folder tujuan kalau belum ada
for key in folders:
    if not os.path.exists(folders[key]):
        os.makedirs(folders[key])

print("=== CARA MAIN ===")
print("[1] Fashion  [2] Rumah  [3] Elektronik  [4] Kesehatan")
print("[S] Skip     [Q] Quit (Keluar)")
print("Klik jendela gambar, lalu tekan tombol keyboard!")

# Loop semua file
files = [f for f in os.listdir(source_folder) if f.endswith((".mp4", ".mov", ".avi"))]

for filename in files:
    filepath = os.path.join(source_folder, filename)

    # Buka video pake OpenCV
    cap = cv2.VideoCapture(filepath)

    # Ambil frame di detik ke-2 (biar gak kena intro item)
    cap.set(cv2.CAP_PROP_POS_MSEC, 2000)
    ret, frame = cap.read()

    if not ret:
        # Kalau gagal baca (file rusak), skip
        cap.release()
        continue

    # Resize biar gak kegedean di layar
    frame = cv2.resize(frame, (600, 800))  # Format HP portrait

    # Tampilkan Gambar
    cv2.imshow("SORTIR KILAT (Tekan 1, 2, 3, 4, S, atau Q)", frame)

    # Tunggu tombol ditekan
    key = cv2.waitKey(0)  # 0 artinya nunggu sampe ditekan

    cap.release()  # Tutup file biar bisa dipindah

    if key == ord("q"):  # Quit
        break

    if key in folders:
        target_folder = folders[key]
        target_path = os.path.join(target_folder, filename)

        # Pindahkan File
        shutil.move(filepath, target_path)
        print(f"✅ {filename} -> {target_folder}")
    else:
        print(f"⏩ Skipped: {filename}")

cv2.destroyAllWindows()
print("Selesai Boss! Istirahat sana.")
