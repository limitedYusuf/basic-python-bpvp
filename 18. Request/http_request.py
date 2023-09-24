import requests

url = 'https://www.example.com'

response = requests.get(url)

if response.status_code == 200:
    print('Permintaan sukses!')
    print('Isi halaman web:')
    print(response.text)
else:
    print('Permintaan gagal. Kode status:', response.status_code)
