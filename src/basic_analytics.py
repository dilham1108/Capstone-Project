import pandas as pd

# Memuat file CSV
file_path = '/mnt/data/MariSehat.csv'
df = pd.read_csv(file_path)

# Menampilkan beberapa baris pertama dari dataset
df.head()

# Rangkuman statistik deskriptif
df.describe()

import matplotlib.pyplot as plt

# Konversi kolom 'Date' menjadi datetime
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

# Plot tren kasus harian
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['New Cases'], label='Kasus Baru', color='blue')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Kasus')
plt.title('Tren Kasus Baru Harian')
plt.legend()
plt.show()

# Plot tren kematian harian
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['New Deaths'], label='Kematian Baru', color='red')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Kematian')
plt.title('Tren Kematian Baru Harian')
plt.legend()
plt.show()

# Menghitung rata-rata rasio fatalitas kasus dan tingkat pemulihan
case_fatality_rate = df['Case Fatality Rate'].str.rstrip('%').astype('float') / 100.0
case_recovered_rate = df['Case Recovered Rate'].str.rstrip('%').astype('float') / 100.0

avg_fatality_rate = case_fatality_rate.mean()
avg_recovered_rate = case_recovered_rate.mean()

avg_fatality_rate, avg_recovered_rate

