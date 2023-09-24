def sapa(nama):
    print("Halo, " + nama + "! Selamat datang.")

sapa("Alice")
sapa("Bob")

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    return hasil

hasil_penjumlahan = tambah(5, 3)
print("Hasil penjumlahan:", hasil_penjumlahan)

def biodata(nama, usia, pekerjaan):
    print("Nama:", nama)
    print("Usia:", usia)
    print("Pekerjaan:", pekerjaan)

biodata(nama="Alice", usia=30, pekerjaan="Insinyur")
biodata(nama="Bob", pekerjaan="Desainer", usia=25)
