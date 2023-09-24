buah = ["apel", "pisang", "ceri", "durian"]

print("Elemen ke-1:", buah[0])
print("Elemen ke-2:", buah[1])
print("Elemen terakhir:", buah[-1])

buah.append("mangga")
print("Setelah menambahkan mangga:", buah)

buah[1] = "jeruk"
print("Setelah mengganti pisang dengan jeruk:", buah)

buah.remove("ceri")
print("Setelah menghapus ceri:", buah)

panjang = len(buah)
print("Panjang list buah:", panjang)

print("Menggunakan perulangan for:")
for buahnya in buah:
    print(buahnya)

if "mangga" in buah:
    print("Mangga ada dalam list.")
else:
    print("Mangga tidak ada dalam list.")
