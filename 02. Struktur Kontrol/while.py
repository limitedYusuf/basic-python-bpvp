angka = 1
while angka <= 5:
    print(angka)
    angka += 1

total = 0
angka = 1
while angka <= 5:
    total += angka
    angka += 1
print("Total:", total)

stop = False
while not stop:
    jawaban = input("Apakah Anda ingin keluar? (ya/tidak) ")
    if jawaban.lower() == "ya":
        stop = True
    else:
        print("Lanjutkan program.")
