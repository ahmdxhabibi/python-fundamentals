# Variable

# Mendeklarasikan variable
nama = "Andi"
usia = 25
tinggi = 165.5

# Menampilkan variable
print("Nama:", nama)  # Output: Nama: Andi
print("Usia:", usia)  # Output: Usia: 25
print("Tinggi:", tinggi)  # Output: Tinggi: 175.5

# Menggunakan variabel dalam operasi
tahun_lahir = 2024 - usia  # Menghitung tahun lahir berdasarkan usia dan tahun saat ini
print("Tahun Lahir:", tahun_lahir)  # Output: Tahun Lahir: 1999


# Mengubah nilai variabel
nama = "Budi"  # Mengubah nilai variabel nama menjadi "Budi"
print("Nama baru:", nama)  # Output: Nama baru: Budi

# Menggabungkan variabel
deskripsi = "Nama saya " + nama + ", usia saya " + \
    str(usia) + " tahun, dan tinggi saya " + str(tinggi) + " cm."
# Output: Nama saya Budi, usia saya 25 tahun, dan tinggi saya 175.5 cm.
print(deskripsi)


"""
Variabel dalam Python tidak perlu dideklarasikan dengan tipe data tertentu sebelumnya,
sehingga sangat fleksibel. Penggunaan variabel memudahkan untuk menyimpan dan
mengelola data yang dapat digunakan di seluruh bagian program.
"""
