# Memahami Penggunaan Loops (for dan while)

# Loop for

# Loop for digunakan untuk iterasi melalui sebuah urutan (seperti list, tuple, dictionary, set, atau string).

# Contoh 1: Iterasi melalui list
angka_list = [1, 2, 3, 4, 5]
for angka in angka_list:
    print("Angka dalam list:", angka)
# Output:
# Angka dalam list: 1
# Angka dalam list: 2
# Angka dalam list: 3
# Angka dalam list: 4
# Angka dalam list: 5

# Contoh 2: Iterasi melalui string
teks = "Python"
for huruf in teks:
    print("Huruf dalam teks:", huruf)
# Output:
# Huruf dalam teks: P
# Huruf dalam teks: y
# Huruf dalam teks: t
# Huruf dalam teks: h
# Huruf dalam teks: o
# Huruf dalam teks: n

# Contoh 3: Iterasi melalui dictionary
kamus = {"nama": "Andi", "usia": 25, "kota": "Jakarta"}
for kunci in kamus:
    print("Kunci:", kunci, "Nilai:", kamus[kunci])
# Output:
# Kunci: nama Nilai: Andi
# Kunci: usia Nilai: 25
# Kunci: kota Nilai: Jakarta

# Loop while

# Loop while digunakan untuk mengulangi eksekusi blok kode selama kondisi yang diberikan bernilai True.

# Contoh 1: Menggunakan while dengan kondisi sederhana
i = 1
while i <= 5:
    print("i adalah:", i)
    i += 1
# Output:
# i adalah: 1
# i adalah: 2
# i adalah: 3
# i adalah: 4
# i adalah: 5

# Contoh 2: Menggunakan while dengan kondisi lebih kompleks
total = 0
angka = 1
while angka <= 100:
    total += angka
    angka += 1
print("Total penjumlahan dari 1 sampai 100 adalah:", total)
# Output:
# Total penjumlahan dari 1 sampai 100 adalah: 5050

# Break dan Continue dalam Loops

# Break: Menghentikan loop sepenuhnya
for angka in range(10):
    if angka == 5:
        break
    print("Angka:", angka)
# Output:
# Angka: 0
# Angka: 1
# Angka: 2
# Angka: 3
# Angka: 4

# Continue: Melompat ke iterasi berikutnya dari loop
for angka in range(10):
    if angka % 2 == 0:
        continue
    print("Angka ganjil:", angka)
# Output:
# Angka ganjil: 1
# Angka ganjil: 3
# Angka ganjil: 5
# Angka ganjil: 7
# Angka ganjil: 9
