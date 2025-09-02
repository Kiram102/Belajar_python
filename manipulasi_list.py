## operasi

data = ["Ucup", "Otong", "Dudung"]

# mengambil data dari list
data_0 = data[0]
print(f"data 0 : {data_0}")

data_terakhir = data[-1]
print(f"data terakhir : {data_terakhir}")

# mengambil info jumlah data
jumlah_data = len(data)
print(f"jumlah data : {jumlah_data}")

## Manipulasi data list

# menambah data list
data.append("Asep")
print(f"data setelah di tambah : {data}")

data.insert(1, "Ujang")
print(f"data setelah di sisipkan : {data}")

# Menambah list dengan list
data_baru = ["Adit", "Adit2", "Adit3"]
data.extend(data_baru)
print(f"data setelah di tambah dengan list : {data}")

# mengubah data list
data[0] = "Kiki"
print(f"data setelah di ubah : {data}")

# menghapus data list
data.remove("Dudung")
print(f"data setelah di hapus : {data}")

# menghapus data paling belakang
data.pop()
print(f"data setelah di pop : {data}")