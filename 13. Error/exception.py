try:
    bilangan1 = int(input("Masukkan bilangan pertama: "))
    bilangan2 = int(input("Masukkan bilangan kedua: "))
    hasil = bilangan1 / bilangan2

    print(f"Hasil pembagian {bilangan1} / {bilangan2} adalah {hasil}")

except ZeroDivisionError:
    print("Pembagian dengan nol tidak diizinkan.")

except ValueError:
    print("Input harus berupa angka.")

except Exception as e:
    print(f"Terjadi kesalahan: {str(e)}")

else:
    print("Pembagian berhasil dilakukan.")

finally:
    print("Program selesai.")
