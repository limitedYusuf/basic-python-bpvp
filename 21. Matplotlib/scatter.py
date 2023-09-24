import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 12, 5, 8, 9]

plt.scatter(x, y, label='Data', color='red', marker='o')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Grafik Scatter')
plt.legend()
plt.show()
