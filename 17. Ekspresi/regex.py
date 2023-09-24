import re

teks = "Halo, nama saya Yusuf. Email saya adalah email_anda@example.com."

pola_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'

hasil_cocok = re.findall(pola_email, teks)

teks_baru = re.sub(pola_email, "yusuf@example.com", teks)

print("Email yang cocok:", hasil_cocok)
print("Teks setelah penggantian:", teks_baru)
