import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]

plt.hist(data, bins=5, edgecolor='black')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.title('Histogram')
plt.show()
