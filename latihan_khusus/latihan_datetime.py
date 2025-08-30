from datetime import datetime as dt

print("Silakan masukan tanggal \nbulan dan tahung lahir")
tanggal = int(input("Masukan Tanggal: \t "))
bulan = int(input("Masukkan Bulan: \t\t "))
tahun = int(input("Masukkan Tahun: \t\t "))

tanggal_lahir = dt(tahun,bulan,tanggal)
print(f"Tanggal Lahir Anda Adalah : {tanggal_lahir}")

hari_ini = dt.today()
print(f"Hari ini adalah : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Harinya adalah : {tanggal_lahir.day}")
print(f"Umur anda adalah : {umur_tahun} tahun, {umur_bulan_sisa} bulan")