# Struktur Data

# List

# List adalah urutan elemen yang dapat diubah dan diindeks.
# List dapat berisi elemen dengan tipe data berbeda.

# Mendefinisikan list
buah = ["apel", "pisang", "ceri"]

# Mengakses elemen dalam list menggunakan indeks
print("Buah pertama:", buah[0])  # Output: Buah pertama: apel

# Menambahkan elemen ke dalam list
buah.append("durian")
# Output: Setelah menambahkan durian: ['apel', 'pisang', 'ceri', 'durian']
print("Setelah menambahkan durian:", buah)

# Menghapus elemen dari list
buah.remove("pisang")
# Output: Setelah menghapus pisang: ['apel', 'ceri', 'durian']
print("Setelah menghapus pisang:", buah)

# Iterasi melalui list
for item in buah:
    print("Buah:", item)
# Output:
# Buah: apel
# Buah: ceri
# Buah: durian

# Tuple

# Tuple adalah urutan elemen yang tidak dapat diubah.
# Tuple dapat berisi elemen dengan tipe data berbeda.

# Mendefinisikan tuple
angka = (1, 2, 3, 4)

# Mengakses elemen dalam tuple menggunakan indeks
print("Angka pertama:", angka[0])  # Output: Angka pertama: 1

# Tuple tidak dapat diubah, tetapi kita dapat melakukan iterasi melalui tuple
for item in angka:
    print("Angka:", item)
# Output:
# Angka: 1
# Angka: 2
# Angka: 3
# Angka: 4

# Dictionary

# Dictionary adalah kumpulan pasangan kunci-nilai.
# Dictionary tidak terurut, dapat diubah, dan diindeks oleh kunci.

# Mendefinisikan dictionary
mahasiswa = {"nama": "Andi", "usia": 21, "jurusan": "Informatika"}

# Mengakses nilai dalam dictionary menggunakan kunci
print("Nama mahasiswa:", mahasiswa["nama"])  # Output: Nama mahasiswa: Andi

# Menambahkan pasangan kunci-nilai ke dalam dictionary
mahasiswa["alamat"] = "Jakarta"
# Output: Setelah menambahkan alamat: {'nama': 'Andi', 'usia': 21, 'jurusan': 'Informatika', 'alamat': 'Jakarta'}
print("Setelah menambahkan alamat:", mahasiswa)

# Menghapus pasangan kunci-nilai dari dictionary
del mahasiswa["usia"]
# Output: Setelah menghapus usia: {'nama': 'Andi', 'jurusan': 'Informatika', 'alamat': 'Jakarta'}
print("Setelah menghapus usia:", mahasiswa)

# Iterasi melalui dictionary
for kunci, nilai in mahasiswa.items():
    print(f"{kunci}: {nilai}")
# Output:
# nama: Andi
# jurusan: Informatika
# alamat: Jakarta

# Set

# Set adalah kumpulan elemen unik yang tidak terurut.
# Set digunakan untuk menyimpan beberapa item dalam satu variabel.

# Mendefinisikan set
himpunan = {1, 2, 3, 4, 4, 5}  # Perhatikan bahwa elemen duplikat akan dihapus

# Menambahkan elemen ke dalam set
himpunan.add(6)
# Output: Setelah menambahkan 6: {1, 2, 3, 4, 5, 6}
print("Setelah menambahkan 6:", himpunan)

# Menghapus elemen dari set
himpunan.remove(3)
# Output: Setelah menghapus 3: {1, 2, 4, 5, 6}
print("Setelah menghapus 3:", himpunan)

# Iterasi melalui set
for item in himpunan:
    print("Elemen:", item)
# Output:
# Elemen: 1
# Elemen: 2
# Elemen: 4
# Elemen: 5
# Elemen: 6

# Contoh Tambahan: Manipulasi List

# Mengurutkan list
buah.sort()
# Output: List buah setelah diurutkan: ['apel', 'ceri', 'durian']
print("List buah setelah diurutkan:", buah)

# Membalik urutan list
buah.reverse()
# Output: List buah setelah dibalik: ['durian', 'ceri', 'apel']
print("List buah setelah dibalik:", buah)

# List comprehension
kuadrat = [x**2 for x in range(10)]
# Output: List kuadrat dari 0 hingga 9: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print("List kuadrat dari 0 hingga 9:", kuadrat)

# Contoh Tambahan: Manipulasi Dictionary

# Menggunakan get() untuk mengakses nilai dengan default
nilai = mahasiswa.get("nilai", "Tidak ada nilai")
print("Nilai mahasiswa:", nilai)  # Output: Nilai mahasiswa: Tidak ada nilai

# Mengupdate dictionary dengan dictionary lain
mahasiswa.update({"nilai": 90, "semester": 5})
# Output: Setelah mengupdate mahasiswa: {'nama': 'Andi', 'jurusan': 'Informatika', 'alamat': 'Jakarta', 'nilai': 90, 'semester': 5}
print("Setelah mengupdate mahasiswa:", mahasiswa)
