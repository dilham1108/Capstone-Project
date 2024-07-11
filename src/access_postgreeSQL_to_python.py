import psycopg2
import pandas as pd

# Koneksi ke database PostgreSQL
conn = psycopg2.connect(
    dbname="nama_database", 
    user="username", 
    password="password", 
    host="localhost"
)

# Query untuk mengambil data
query = "SELECT * FROM covid_cases;"

# Membaca data ke DataFrame Pandas
df = pd.read_sql(query, conn)

# Menampilkan beberapa baris pertama dari dataset
print(df.head())

# Menutup koneksi
conn.close()
