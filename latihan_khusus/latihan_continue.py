attempt = 0
max_attempts = 3

while attempt < max_attempts:
    print("Login Sederhana")
    
    input_n = input("Masukan Nama : ")
    input_p = input("Masukan Pass word : ")

    if input_n == "" or input_p == "" :
        print("Nama Dan Password Harus Disi")
        continue
    
    attempt += 1

    if input_n == "Kiki" and input_p == "123" :
        print("Login Berhasil")
        break
    else :
        remaining = max_attempts - attempt
        if remaining > 0 :
            print(f"Sisa Kesempatan : {remaining}")
        else :
            print("Akun Terkunci")