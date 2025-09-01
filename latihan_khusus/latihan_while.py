pilihan = 0

while pilihan != 4 :
    print("\n=== MENU ===")
    print("1. Tambah")
    print("2. Kali") 
    print("3. Bagi")
    print("4. Keluar")

    pilihan = int(input("Masukan Pilihan : "))


    if pilihan == 4 :
        print("Anda Keluar")
        break

    if pilihan in [1,2,3] :
        angka1 = int(input("Masukan Angka 1 :"))
        angka2 = int(input("Masukan Angka 2 :"))

        if pilihan == 1 :
            hasil = angka1 + angka2
            print(f"{angka1} + {angka2} = {hasil}")
        elif pilihan == 2 :
            hasil = angka1 * angka2
            print(f"{angka1} X {angka2} = {hasil}")
        elif pilihan == 3 :
            hasil = angka1 / angka2
            print(f"{angka1} : {angka2} = {hasil}")
        else : 
            print("Pilihan Tidak Ada")