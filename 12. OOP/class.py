class Kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def menggonggong(self):
        print(f"{self.nama} menggonggong!")

    def dapatkan_umur(self):
        return self.umur

kucing1 = Kucing("Meow", 2)
kucing2 = Kucing("Whiskers", 3)

print(f"{kucing1.nama} adalah seekor kucing berumur {kucing1.dapatkan_umur()} tahun.")
print(f"{kucing2.nama} adalah seekor kucing berumur {kucing2.dapatkan_umur()} tahun.")
kucing1.menggonggong()
kucing2.menggonggong()
