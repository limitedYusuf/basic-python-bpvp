teks = "Python Programming"
teks_besar = teks.upper()
teks_kecil = teks.lower()

print("Teks asli:", teks)
print("Huruf besar:", teks_besar)
print("Huruf kecil:", teks_kecil)

teks_strip = "  Spasi di awal dan akhir  "
teks_tanpa_spasi = teks_strip.strip()

print("Teks asli:", teks_strip)
print("Teks tanpa spasi:", teks_tanpa_spasi)

# Menggunakan metode split()
kalimat = "Halo, selamat datang di Python"
kata_kunci = kalimat.split(", ")

print("Kata-kata:", kata_kunci)

kata_kunci = ["Halo", "selamat", "datang", "di", "Python"]
kalimat_baru = ", ".join(kata_kunci)

print("Kalimat baru:", kalimat_baru)

indeks = kalimat.find("selamat")
print("Indeks kata 'selamat':", indeks)

kalimat_baru = kalimat.replace("Python", "Java")
print("Kalimat baru setelah penggantian:", kalimat_baru)

jumlah = kalimat.count("a")
print("Jumlah kemunculan huruf 'a':", jumlah)
