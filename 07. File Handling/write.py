import os

folder_handle = "07. File Handling"

file_path = os.path.join(folder_handle, "dummy.txt")

try:
    with open(file_path, 'w') as file:
        file.write("Ini adalah contoh kalimat.\n")
        file.write("Ini adalah baris kedua dari contoh.\n")
        print("Teks berhasil ditulis ke file.")

except Exception as e:
    print("Terjadi kesalahan:", str(e))
