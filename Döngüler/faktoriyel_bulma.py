print("""
*******************
FAKTÖRİYEL BULMA PROGRAMI

Çıkmak için q'ya basınız
*******************
""")
while True:
    sayı=input("sayı:")
    if(sayı == "q"):
        print("Programınız Sonlandırılıyor....")
        break
    else:
        sayı = int(sayı)
        faktoriyel = 1
        for i in range(2,sayı+1):
            print("FAKTORİYEL",faktoriyel,"i:",i)
            faktoriyel *= i
        print("FAKTORİYEL",faktoriyel)