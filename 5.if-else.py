# Pengambilan Keputusan Menggunakan if, elif, dan else

umur = 25

# Menggunakan if
if umur < 13:
    print("Kategori: Anak-anak")
# Menggunakan elif
elif 13 <= umur < 18:
    print("Kategori: Remaja")
# Menggunakan elif lain
elif 18 <= umur < 60:
    print("Kategori: Dewasa")  # Output: Kategori: Dewasa
# Menggunakan else
else:
    print("Kategori: Lansia")

# Contoh tambahan: Penggunaan operator logika dalam pengambilan keputusan

nilai = 85

# Menggunakan if dengan operator logika
if nilai >= 90:
    print("Nilai Anda: A")
elif nilai >= 80 and nilai < 90:
    print("Nilai Anda: B")  # Output: Nilai Anda: B
elif nilai >= 70 and nilai < 80:
    print("Nilai Anda: C")
elif nilai >= 60 and nilai < 70:
    print("Nilai Anda: D")
else:
    print("Nilai Anda: E")
