#data default nya string
data = input("Masukan Data :")

print("Data :", data, type(data))

#jika tidak mau sting maka lakukan ini
angka = int(input("Masukan Angka :"))
angka = float(input("Masukan Angka :"))

print("Angka :", angka, type(angka))

#jika mau boolean
bool = bool(int(input("Masukan Angka :")))
print("Data :", bool, type(bool))