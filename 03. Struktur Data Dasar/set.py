buah_set = {"apel", "pisang", "ceri", "durian"}

buah_set.add("mangga")
print("Setelah menambahkan mangga:", buah_set)

buah_set.remove("ceri")
print("Setelah menghapus ceri:", buah_set)

jumlah_elemen = len(buah_set)
print("Jumlah elemen dalam set buah_set:", jumlah_elemen)

print("Menggunakan perulangan for:")
for buah in buah_set:
    print(buah)

if "mangga" in buah_set:
    print("Mangga ada dalam set buah_set.")
else:
    print("Mangga tidak ada dalam set buah_set.")

buah_set2 = {"apel", "anggur", "nanas"}
gabungan = buah_set.union(buah_set2)
print("Hasil gabungan dua set:", gabungan)

irisan = buah_set.intersection(buah_set2)
print("Hasil irisan dua set:", irisan)

perbedaan = buah_set.difference(buah_set2)
print("Hasil perbedaan dua set:", perbedaan)
