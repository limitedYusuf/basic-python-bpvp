umur = int(input("Masukkan umur Anda: "))

# if, elif, dan else
if umur < 18:
    print("Anda masih anak-anak.")
elif 18 <= umur < 60:
    print("Anda adalah seorang dewasa.")
else:
    print("Anda adalah seorang senior.")

print("Terima kasih telah menggunakan program ini!")
