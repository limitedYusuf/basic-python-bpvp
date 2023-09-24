for angka in range(1, 6):
    print(angka)

total = 0
for angka in range(1, 6):
    total += angka
print("Total:", total)

buah = ["apel", "pisang", "ceri", "durian"]
for buahnya in buah:
    print("Saya suka", buahnya)

for indeks, buahnya in enumerate(buah):
    print("Indeks:", indeks, "Buah:", buahnya)
