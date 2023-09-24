import json
import os

folder_handle = "15. File JSON"

file_path = os.path.join(folder_handle, "dummy.json")

try:
    with open(file_path, 'r') as file:
        data = json.load(file)
        print("Data yang dibaca dari file JSON:")
        print(data)
except FileNotFoundError:
    print("File JSON tidak ditemukan.")
except json.JSONDecodeError as e:
    print(f"Terjadi kesalahan dalam membaca file JSON: {str(e)}")
