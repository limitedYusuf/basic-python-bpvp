import os

folder_handle = "07. File Handling"

file_path = os.path.join(folder_handle, "dummy.txt")

try:
    with open(file_path, 'r') as file:
        isi_file = file.read()
        print("Isi file:")
        print(isi_file)

except FileNotFoundError:
    print("File tidak ditemukan.")
except Exception as e:
    print("Terjadi kesalahan:", str(e))
