# Module adalah file yang berisi definisi dan pernyataan Python.

# Contoh 1: Mengimpor Module Standar

# Mengimpor module math untuk operasi matematika
import contoh_module
import datetime as dt
from math import sin, cos
import math

# Menggunakan fungsi sqrt dari module math
akar = math.sqrt(16)
# Output: Akar kuadrat dari 16 adalah: 4.0
print("Akar kuadrat dari 16 adalah:", akar)

# Menggunakan konstanta pi dari module math
lingkaran_luas = math.pi * (5 ** 2)
# Output: Luas lingkaran dengan radius 5 adalah: 78.53981633974483
print("Luas lingkaran dengan radius 5 adalah:", lingkaran_luas)

# Contoh 2: Mengimpor Fungsi atau Variabel Tertentu dari Module

# Mengimpor fungsi sin dan cos dari module math

sudut = math.radians(90)  # Mengonversi derajat ke radian
nilai_sin = sin(sudut)
nilai_cos = cos(sudut)
# Output: Sin 90 derajat adalah: 1.0
print("Sin 90 derajat adalah:", nilai_sin)
# Output: Cos 90 derajat adalah: 6.123233995736766e-17 (mendekati 0)
print("Cos 90 derajat adalah:", nilai_cos)

# Contoh 3: Mengimpor Module dengan Alias

# Mengimpor module datetime dengan alias dt

# Menggunakan module datetime untuk mendapatkan tanggal dan waktu saat ini
waktu_sekarang = dt.datetime.now()
print("Waktu saat ini adalah:", waktu_sekarang)

# Contoh 4: Membuat dan Mengimpor Contoh Modul

# Misalkan kita punya file `contoh_modul.py` dengan isi berikut:
# def salam(nama):
#     return f"Halo, {nama}!"

# Mengimpor modul sendiri

# Menggunakan fungsi dari module sendiri
pesan_salam = contoh_module.salam("Andi")
print(pesan_salam)  # Output: Halo, Andi!
