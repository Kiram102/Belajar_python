from datetime import datetime as dt

print(f"{'Form Data Diri':-^30}")

nama = str(input("Masukan Nama Anda :"))
kelas = str(input("Masukan Kelas Anda :"))
tahun_lahir = int(input("Masukan Tahun Lahir :"))
bulan_lahir = int(input("Masukan Bulan Lahir :"))
tanggal_lahir = int(input("Masukan Tanggal Lahir :"))

birth = dt(tahun_lahir,bulan_lahir,tanggal_lahir)

print(f"{'Nama':<10} | {'Kelas':<10} | {'Tanggal Lahir':<12}")
print("-" * 40)
print(f"{nama:<10} | {kelas:<10} | {birth.strftime('%d-%m-%Y'):<12}")