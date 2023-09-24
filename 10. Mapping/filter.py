def adalah_genap(x):
    return x % 2 == 0

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

bilangan_genap = list(filter(adalah_genap, angka))
print("Bilangan genap dalam list:", bilangan_genap)
