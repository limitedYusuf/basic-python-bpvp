class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def bersuara(self):
        pass

class Kucing(Hewan):
    def bersuara(self):
        return f"{self.nama} menggonggong!"

class Anjing(Hewan):
    def bersuara(self):
        return f"{self.nama} mengeong!"

kucing1 = Kucing("Meow", "Kucing")
anjing1 = Anjing("Whiskers", "Anjing")

print(kucing1.bersuara())
print(anjing1.bersuara())
