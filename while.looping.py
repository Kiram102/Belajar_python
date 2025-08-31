# i = 1
# while i <= 5 :
#     print(i)
#     i += 1

# password = ""
# while password != "rahasia" :
#     password = input("Masukan Password : ")
#     if password != "rahasia" :
#         print("Ulang")
# print("Login Berhasil")

pilihan = 0

while pilihan != 4 :
    print("\n=== MENU ===")
    print("1. Tambah Data")
    print("2. Lihat Data") 
    print("3. Hapus Data")
    print("4. Keluar")

    pilihan = int(input("Masukan Pilihan : "))
    
    if pilihan == 1:
        print("Tambah Data")
    elif pilihan == 2:
        print("Lihat Data")
    elif pilihan == 3:
        print("Hapus Data")
    elif pilihan == 4:
        print("Keluar program...")
    else :
        print("Pilihan Tidak Ada")