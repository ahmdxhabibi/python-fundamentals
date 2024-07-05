# Memahami Fungsi dalam Python

# Definisi dan Pemanggilan Fungsi

# Mendefinisikan fungsi tanpa parameter dan nilai pengembalian
def halo_dunia():
    # Fungsi ini mencetak "Halo, Dunia!" ke layar
    print("Halo, Dunia!")


# Memanggil fungsi tanpa parameter
halo_dunia()  # Output: Halo, Dunia!

# Mendefinisikan fungsi dengan satu parameter


def salam(nama):
    # Fungsi ini mencetak pesan salam dengan nama yang diberikan sebagai argumen
    print("Halo,", nama)


# Memanggil fungsi dengan argumen
salam("Andi")  # Output: Halo, Andi

# Mendefinisikan fungsi dengan dua parameter dan nilai pengembalian


def tambah(a, b):
    # Fungsi ini mengembalikan hasil penjumlahan dari dua argumen
    return a + b


# Memanggil fungsi dengan argumen dan menangkap nilai pengembalian
hasil = tambah(5, 3)
print("Hasil penjumlahan:", hasil)  # Output: Hasil penjumlahan: 8

# Parameter dan Argumen

# Mendefinisikan fungsi dengan parameter default


def salam_default(nama="Teman"):
    # Fungsi ini mencetak pesan salam dengan nama yang diberikan, atau "Teman" jika tidak ada nama yang diberikan
    print("Halo,", nama)


# Memanggil fungsi tanpa argumen
salam_default()  # Output: Halo, Teman

# Memanggil fungsi dengan argumen
salam_default("Budi")  # Output: Halo, Budi

# Nilai Pengembalian

# Fungsi dengan beberapa pernyataan return


def cek_angka(angka):
    # Fungsi ini mengembalikan status angka (Positif, Negatif, atau Nol)
    if angka > 0:
        return "Positif"
    elif angka < 0:
        return "Negatif"
    else:
        return "Nol"


# Memanggil fungsi dengan argumen dan menangkap nilai pengembalian
status = cek_angka(5)
print("Status angka:", status)  # Output: Status angka: Positif

# Contoh Tambahan

# Mendefinisikan fungsi dengan lebih dari dua parameter


def operasi_matematika(a, b, operasi):
    # Fungsi ini melakukan operasi matematika sesuai dengan parameter operasi
    if operasi == "tambah":
        return a + b
    elif operasi == "kurang":
        return a - b
    elif operasi == "kali":
        return a * b
    elif operasi == "bagi":
        return a / b
    else:
        return "Operasi tidak dikenal"


# Memanggil fungsi dengan argumen
hasil_tambah = operasi_matematika(10, 5, "tambah")
hasil_kurang = operasi_matematika(10, 5, "kurang")
hasil_kali = operasi_matematika(10, 5, "kali")
hasil_bagi = operasi_matematika(10, 5, "bagi")
hasil_salah = operasi_matematika(10, 5, "modulo")

print("Hasil tambah:", hasil_tambah)  # Output: Hasil tambah: 15
print("Hasil kurang:", hasil_kurang)  # Output: Hasil kurang: 5
print("Hasil kali:", hasil_kali)  # Output: Hasil kali: 50
print("Hasil bagi:", hasil_bagi)  # Output: Hasil bagi: 2.0
print("Hasil salah:", hasil_salah)  # Output: Operasi tidak dikenal
