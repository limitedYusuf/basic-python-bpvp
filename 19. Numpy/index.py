import numpy as np

data = np.array([1, 2, 3, 4, 5])

print("Array NumPy:")
print(data)

mean = np.mean(data)
median = np.median(data)
std_deviation = np.std(data)

print("\nStatistik data:")
print("Rata-rata:", mean)
print("Median:", median)
print("Standar Deviasi:", std_deviation)

data_plus_2 = data + 2
data_squared = data ** 2

print("\nOperasi pada array:")
print("Array ditambah 2:", data_plus_2)
print("Array kuadrat:", data_squared)

max_value = np.max(data)
min_value = np.min(data)
sum_values = np.sum(data)

print("\nFungsi-fungsi NumPy lainnya:")
print("Nilai maksimum:", max_value)
print("Nilai minimum:", min_value)
print("Jumlah semua elemen:", sum_values)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("\nArray 2D:")
print(matrix)

transposed_matrix = np.transpose(matrix)

print("\nTransposisi array 2D:")
print(transposed_matrix)
