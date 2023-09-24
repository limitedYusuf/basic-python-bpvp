import json
import os

folder_handle = "15. File JSON"

file_path = os.path.join(folder_handle, "dummy.json")

data = {
    "nama": "John",
    "umur": 30,
    "kota": "New York"
}

try:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print("Data berhasil ditulis ke file JSON.")
except Exception as e:
    print(f"Terjadi kesalahan dalam menulis file JSON: {str(e)}")
