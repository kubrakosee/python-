"""
                                   KULLANICIDAN AD,SOYAD VE NUMARA BİLGİSİNİ ALARAK BUNLARI
                                              ALT ALTA EKRANA YAZDIRIN
"""


ad=input("adınızı giriniz:")
soyad=input("soyadınızı giriniz:")

numara=int(input("numaranızı giriniz:"))
print("\n Bilgiler Yazılıyor...\n")

"""
print("adınız:{}\nsoyadınız:{}\nNumaranız:{}\n".format(ad,soyad,numara))
her iki türlüde olabilir.

"""

print("{}\n{}\n{}\n".format(ad,soyad,numara))