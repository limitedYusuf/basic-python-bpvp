buah = ("apel", "pisang", "ceri", "durian")

print("Elemen ke-1:", buah[0])
print("Elemen ke-2:", buah[1])
print("Elemen terakhir:", buah[-1])

panjang = len(buah)
print("Panjang tuple buah:", panjang)

print("Menggunakan perulangan for:")
for buahnya in buah:
    print(buahnya)

if "mangga" in buah:
    print("Mangga ada dalam tuple.")
else:
    print("Mangga tidak ada dalam tuple.")
