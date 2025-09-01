from datetime import datetime as dt

nama = str(input("Masukan Nama :"))
kelas = str(input("Masukan Kelas :"))
hobi = str(input("Masukan Hobi :"))
tanggal_lahir = str(input("Masukan Tanggal Lahir (DD/MM/YYYY) :"))

tanggal_lahir_parshed = dt.strptime(tanggal_lahir, "%d/%m/%Y")

hasil = nama,kelas,hobi,tanggal_lahir_parshed

for i in hasil :
    print(f"Saya : {i}")