print("Taş - Kağıt - Makas oyununa Hoşgeldiniz...\nOyun Yükleniyor...\n"
        "Lütfen 'taş, kağıt, makas tercihlerinden birini yapınız'")

player1 = input("1. Oyuncu Lütfen Adınız Giiniz: ")
player2 = input("2. Oyuncu Lütfen Adınız Giriniz: ")

x = 1
y = 0 #Birinci oyuncunun skoru
z = 0 #ikinci oyuncunun skoru

while x <= 10:
    choice1 = input(f"{player1} Lütfen Tercihinizi Giriniz: ")
    choice2 = input(f"{player2} Lütfen Tercihinizi Giriniz: ")

    if choice1 == choice2:
        print("Berabere kaldınız.")
        y = y + 1
        z = z + 1
    elif choice1 == "taş" and choice2 == "makas" or choice1 == "kağıt" and choice2 == "taş" or choice1 == "makas" and choice2 == "kağıt":
        print(f"{player1} Kazandınız...")
        y = y + 1
    else:
        print(f"{player2} Kazandınız")
        z = z + 1
    x = x + 1
    
print(f"{player1} skorunuz: {y}")
print(f"{player2} skorunuz: {z}")

if y == z:
    print(f"{player1} ve {player2} berabere kaldınız...")
elif y > z:
    print(f"{player1} Tebrikler Kazandınız!!!")
else:
    print(f"{player2} Tebrikler Kazandınız!!!")




