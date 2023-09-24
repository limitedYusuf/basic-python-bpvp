class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.__nim = nim

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        if len(nim) == 8:
            self.__nim = nim
        else:
            print("NIM harus terdiri dari 8 karakter.")

mahasiswa1 = Mahasiswa("Alice", "12345678")

print(f"Nama: {mahasiswa1.nama}")
print(f"NIM: {mahasiswa1.get_nim()}")

mahasiswa1.set_nim("87654321")
print(f"NIM setelah perubahan: {mahasiswa1.get_nim()}")
