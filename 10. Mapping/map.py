def kuadrat(x):
    return x ** 2

angka = [1, 2, 3, 4, 5]

hasil_kuadrat = list(map(kuadrat, angka))
print("Hasil kuadrat dari setiap angka:", hasil_kuadrat)
