"""

                                      KULLANICIDAN ALDIĞINIZ BOY VE KİLO DEĞERLERİNE GÖRE
                                         KULLANICIDAN BEDEN KİTLE İNDEKSİNİ BULUNUZ
"""

kilo=int(input("Kilonuzu Giriniz.."))
boy=float(input("Boyunuzu Giriniz.."))
indeks=(kilo/(boy**2))

print("boyunuz:{}\nkilonuz:{}\nindeksiniz:{}".format(boy,kilo,indeks))
"""

kilo=int(input("Kilonuzu Giriniz.."))
boy=float(input("Boyunuzu Giriniz.."))
print("Beden Kitle İndeksi:",kilo/(boy **2))

böylede olabilir.her iki türlü de doğru çalışıyor.
"""