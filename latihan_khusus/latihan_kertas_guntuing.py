import random

option = ['kertas' , 'gunting' , 'batu']
running = True

while running :
    player = None
    computer = random.choice(option)

    while player not in option :
        player = input("Masukan Kertas Gunting Batu : ").lower()

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer :
        print("Seri")
    elif player == "kertas" and computer == "batu" :
        print("Menang")
    elif player == "gunting" and computer == "kertas" :
        print("Menang")
    elif player == "batu" and computer == "gunting" :
        print("Menang")
    else :
        print("Anda Kalah")

    lanjut = input("Pencet q Bila ingin selesai Pencet Yang Lain Bila Ingin Lanjut : ").lower()

    if lanjut == "q" :
        print("Keluar")
        break
    
print("Terimakasih")