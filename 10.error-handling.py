# Error Handling

# Penanganan error digunakan untuk mengatasi kesalahan yang terjadi selama eksekusi program.
# Dengan menangani error, kita dapat mencegah program berhenti secara tiba-tiba dan memberikan pesan kesalahan yang lebih informatif.

# Struktur Dasar Try-Except

try:
    # Blok kode yang mungkin menghasilkan error
    hasil = 10 / 0
except ZeroDivisionError:
    # Blok kode ini akan dieksekusi jika terjadi ZeroDivisionError
    print("Terjadi error: Pembagian dengan nol tidak diperbolehkan.")
# Output: Terjadi error: Pembagian dengan nol tidak diperbolehkan.

# Menggunakan Blok Else

try:
    # Blok kode yang mungkin menghasilkan error
    hasil = 10 / 2
except ZeroDivisionError:
    # Blok kode ini akan dieksekusi jika terjadi ZeroDivisionError
    print("Terjadi error: Pembagian dengan nol tidak diperbolehkan.")
else:
    # Blok kode ini akan dieksekusi jika tidak terjadi error
    print("Hasil:", hasil)
# Output: Hasil: 5.0

# Menggunakan Blok Finally

try:
    # Blok kode yang mungkin menghasilkan error
    hasil = 10 / 2
except ZeroDivisionError:
    # Blok kode ini akan dieksekusi jika terjadi ZeroDivisionError
    print("Terjadi error: Pembagian dengan nol tidak diperbolehkan.")
else:
    # Blok kode ini akan dieksekusi jika tidak terjadi error
    print("Hasil:", hasil)
finally:
    # Blok kode ini akan dieksekusi apapun yang terjadi
    print("Eksekusi blok finally selesai.")
# Output:
# Hasil: 5.0
# Eksekusi blok finally selesai.

# Menangani Berbagai Jenis Error

try:
    # Blok kode yang mungkin menghasilkan berbagai jenis error
    angka = int("abc")
except ValueError:
    # Blok kode ini akan dieksekusi jika terjadi ValueError
    print("Terjadi error: Nilai tidak dapat dikonversi ke integer.")
except ZeroDivisionError:
    # Blok kode ini akan dieksekusi jika terjadi ZeroDivisionError
    print("Terjadi error: Pembagian dengan nol tidak diperbolehkan.")
# Output: Terjadi error: Nilai tidak dapat dikonversi ke integer.

# Memunculkan (Raise) Exception


def cek_positif(angka):
    if angka < 0:
        # Memunculkan exception jika angka negatif
        raise ValueError("Nilai harus positif.")
    return angka


try:
    hasil = cek_positif(-5)
except ValueError as e:
    # Menangani exception dan mencetak pesan kesalahan
    print("Terjadi error:", e)
# Output: Terjadi error: Nilai harus positif.

# Contoh Tambahan: Membuat Exception Kustom

# Mendefinisikan exception kustom


class ErrorKustom(Exception):
    def __init__(self, pesan):
        self.pesan = pesan

# Fungsi yang memunculkan exception kustom


def cek_nilai(nilai):
    if nilai < 0:
        raise ErrorKustom("Nilai tidak boleh negatif.")
    return nilai


try:
    hasil = cek_nilai(-10)
except ErrorKustom as e:
    # Menangani exception kustom dan mencetak pesan kesalahan
    print("Terjadi error kustom:", e.pesan)
# Output: Terjadi error kustom: Nilai tidak boleh negatif.
