mahasiswa = {
    "nama": "John Doe",
    "usia": 22,
    "jurusan": "Informatika",
    "nim": "12345"
}

print("Nama:", mahasiswa["nama"])
print("Usia:", mahasiswa["usia"])
print("Jurusan:", mahasiswa["jurusan"])
print("NIM:", mahasiswa["nim"])

mahasiswa["usia"] = 23
print("Usia setelah diubah:", mahasiswa["usia"])

mahasiswa["alamat"] = "Jl. Contoh No. 123"
print("Alamat:", mahasiswa["alamat"])

del mahasiswa["nim"]
print("Setelah menghapus NIM:", mahasiswa)

jumlah_data = len(mahasiswa)
print("Jumlah data dalam kamus mahasiswa:", jumlah_data)

print("Menggunakan perulangan for:")
for kunci, nilai in mahasiswa.items():
    print(kunci + ":", nilai)

if "jurusan" in mahasiswa:
    print("Jurusan ada dalam kamus mahasiswa.")
else:
    print("Jurusan tidak ada dalam kamus mahasiswa.")
