import matplotlib.pyplot as plt

kategori = ['A', 'B', 'C', 'D', 'E']
jumlah = [10, 15, 7, 12, 9]

plt.bar(kategori, jumlah)
plt.xlabel('Kategori')
plt.ylabel('Jumlah')
plt.title('Diagram Batang')
plt.show()
