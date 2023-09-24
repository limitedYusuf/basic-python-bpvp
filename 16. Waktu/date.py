import datetime

sekarang = datetime.datetime.now()
print("Tanggal dan Waktu Sekarang:", sekarang)

tahun = sekarang.year
bulan = sekarang.month
hari = sekarang.day
jam = sekarang.hour
menit = sekarang.minute
detik = sekarang.second

print(f"Tahun: {tahun}, Bulan: {bulan}, Hari: {hari}")
print(f"Jam: {jam}, Menit: {menit}, Detik: {detik}")

format_tanggal = sekarang.strftime("%d-%m-%Y")
format_waktu = sekarang.strftime("%H:%M:%S")
print(f"Format Tanggal: {format_tanggal}")
print(f"Format Waktu: {format_waktu}")

tanggal_awal = datetime.datetime(2023, 1, 1)
tanggal_sekarang = datetime.datetime.now()
selisih = tanggal_sekarang - tanggal_awal
print(f"Selisih waktu dari 1 Januari 2023: {selisih}")
