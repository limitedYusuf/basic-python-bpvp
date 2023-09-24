nama = "Alice"
umur = 30
tinggi = 165.5

teks = f"Nama: {nama}, Usia: {umur}, Tinggi: {tinggi} cm"
print(teks)

nilai1 = 85
nilai2 = 92

teks_format = "Nilai 1: {:.2f}, Nilai 2: {:.2f}".format(nilai1, nilai2)
print(teks_format)

harga = 75.50
diskon = 15

teks_diskon = "Harga: %.2f, Diskon: %d%%" % (harga, diskon)
print(teks_diskon)

nama_barang = "Laptop"
harga_barang = 1000

teks_barang = "Barang: {}, Harga: ${}".format(nama_barang, harga_barang)
print(teks_barang)
