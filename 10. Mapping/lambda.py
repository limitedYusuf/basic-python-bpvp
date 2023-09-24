kuadrat = lambda x: x ** 2

angka = 5
hasil = kuadrat(angka)
print(f"Kuadrat dari {angka} adalah {hasil}")

gabung_string = lambda a, b: a + " " + b

teks1 = "Halo,"
teks2 = "dunia!"
gabungan = gabung_string(teks1, teks2)
print(gabungan)

bilangan = [1, 2, 3, 4, 5]
hasil_kuadrat = list(map(lambda x: x ** 2, bilangan))
print("Hasil kuadrat dari setiap bilangan:", hasil_kuadrat)
