try:
    hasil = 10 / 0

except ZeroDivisionError:
    print("Terjadi pembagian dengan nol.")

except Exception as e:
    print("Terjadi pengecualian:", str(e))

finally:
    print("Blok finally selalu dijalankan.")

print("Kode berlanjut setelah penanganan pengecualian.")
