# 1. menyambung string (concatenate)
nama_pertama = "kiki"
nama_akhir = "Ramdani"

nama_lengkap = nama_pertama + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string

k = "kiki"
status = k in nama_lengkap
print("string " + k + " ada di " + nama_lengkap + str(status))

k = "KIKI"
status = k in nama_lengkap
print("string " + k + " ada di " + nama_lengkap + str(status))

k = "kiki"
status = k not in nama_lengkap
print("string " + k + " tidak ada di " + nama_lengkap + str(status))

# mengulang string 
print("KIKI "*10)

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[6])
print("index ke-(-1) : " + nama_lengkap[-2])
print("index ke-[0,6] : " + nama_lengkap[0:3])
print("index ke-[0,2,6,8,11] : " + nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))

# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII CODE untuk spasi adalah " + str(ascii_code))

data = 117
print("Char untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method
data = "Miaw wongireng"
jumlah = data.count('i')
print("jumlah i pada " + data + "= " + str(jumlah))