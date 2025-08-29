# operator dalam bentuk methods

## merubah case jadi string

# merubah semua ke upper case

nama = "kiki"
print("normal = " + nama)
nama = nama.upper()
print("upper = " + nama)

# merubah ke lower case

miaw = "AkkkLos"
print("normal = " + miaw)
miaw = miaw.lower()
print("lower = " + miaw)

## pengecekan dengan isX method

# contoh untuk pengecekan lowe case

nama = "komi"
apakah_lower = nama.islower() # hasilnya boolean
print(nama + "is lower = " + str(apakah_lower))
apakah_upper = nama.isupper()
print(nama + "is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- untuk huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle() <-- semua kata dimulai dengan huruf besar

kata = "Skiki23"

is_alpha = kata.isalpha()
print(kata + "is alpha = " + str(is_alpha))

is_enum = kata.isalnum()
print(kata + "is alnum = " + str(is_enum))

is_decimal = kata.isdecimal()
print(kata + "is decimal = " + str(is_decimal))

is_space = kata.isspace()
print(kata + "is space = " + str(is_space))

is_title = kata.istitle()
print(kata + "is title = " + str(is_title))

## ngecek komponen startswith() endswith()

cek_start = "Miaw Miawa".startswith("Miaw")
print("Start = " + str(cek_start))

cek_end = "Miaw Miawa".endswith("Miawa")
print("Start = " + str(cek_end))

## penggabungan komponen join() split()

pisah = ['kiki','ramdani','miaw']
print(pisah)

join = '.'.join(pisah)
print(join)

pisah = "aku.sayang.kamu"
print(pisah.split('.'))

# alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

center = "center".center(10,"-")
print("'"+center+"'")

# kebalikannya -> strip() menghilangkan tanda tanda
center = "center".strip("-")
print("'"+center+"'")