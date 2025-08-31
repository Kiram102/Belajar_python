# nama = str(input("Masukan Nama :"))

# if nama == "kiki" :
#     print("Kamu Keren")
# else :
#     print(f"{nama} Gak Di Ajak")

print(f"{'Pilih Aritmatika':-^30}")
print("Ketik 1 Untuk Pilih Perkalian")
print("Keting 2 Untuk Pilih Tambah")

pilihan = int(input("Pilihan Anda :"))


if pilihan == 1 or pilihan == 2:
    angka1 = int(input("Angka Pertama :"))
    angka2 = int(input("Angka Kedua :"))
    if pilihan == 1 :
        hasil = angka1 * angka2
        print(f"'{angka1} X {angka2} = {hasil}'")
    elif pilihan == 2 :
        hasil = angka1 + angka2
        print(f"'{angka1} + {angka2} = {hasil}'")
else :
    print("Pilihan Tidak Ada")

