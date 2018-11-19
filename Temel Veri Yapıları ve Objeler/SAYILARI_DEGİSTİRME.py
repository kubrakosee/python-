"""
                                      KULLANICIDAN İKİ TANE SAYI İSTEYİN VE BU SAYILARIN
                                            DEĞERLERİNİ BİRBİRLERİYLE DEĞİŞTİRİN

"""


a=int(input("birinci sayıyı giriniz:"))
b=int(input("ikinci sayıyı giriniz:"))
print("değiştirilmeden önceki değerler \na:{}\nb:{}\n".format(a,b))
a,b=b,a
print("değiştirildikten sonraki değerler \na:{}\nb:{}\n".format(a,b))