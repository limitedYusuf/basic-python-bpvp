import os
import sys
import math

current_directory = os.getcwd()
print("Direktori saat ini:", current_directory)

print("Argumen baris perintah:", sys.argv)

angka = 16
akar_kuadrat = math.sqrt(angka)
print(f"Akar kuadrat dari {angka} adalah {akar_kuadrat}")

pi = math.pi
print(f"Nilai Pi: {pi}")
