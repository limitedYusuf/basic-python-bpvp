from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

class Segitiga(Bentuk):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

segitiga1 = Segitiga(6, 4)

print(f"Luas segitiga: {segitiga1.luas()}")
