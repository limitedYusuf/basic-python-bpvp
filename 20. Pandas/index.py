import pandas as pd

data = {'Nama': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Usia': [25, 30, 35, 28, 24],
        'Kota': ['Jakarta', 'Surabaya', 'Bandung', 'Jakarta', 'Surabaya']}

df = pd.DataFrame(data)

print("Data awal:")
print(df)

print("\nInformasi tentang DataFrame:")
print(df.info())

print("\nStatistik deskriptif:")
print(df.describe())

filtered_data = df[df['Usia'] > 30]

print("\nData yang usianya di atas 30:")
print(filtered_data)

df['Jenis Kelamin'] = ['P', 'L', 'L', 'L', 'P']

print("\nDataFrame setelah menambahkan kolom 'Jenis Kelamin':")
print(df)

df = df.drop(columns=['Jenis Kelamin'])

print("\nDataFrame setelah menghapus kolom 'Jenis Kelamin':")
print(df)
