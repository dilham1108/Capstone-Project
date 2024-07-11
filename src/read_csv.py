import pandas as pd

# Memuat file CSV
file_path = '/mnt/data/MariSehat.csv'
df = pd.read_csv(file_path)

# Menampilkan beberapa baris pertama dari dataset
df.head()
