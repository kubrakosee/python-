print("""******************************

HESAP MAKİNESİ PROGRAMI

İŞLEMLER

1.TOPLAMA İŞLEMİ

2.ÇIKARMA İŞLEMİ

3.ÇARPMA İŞLEMİ

4.BÖLME İŞLEMİ

**************************************
""")
a=int(input("birinci sayı.."))
b=int(input("ikinci sayı.."))

islem=input("işlemi giriniz..")

if islem=="1":
    print("{} ile {} in toplamı {} dir.".format(a,b,a+b))

elif islem=="2":
    print("{} ile {} in çıkarma {} dir.".format(a, b,a-b))
elif islem=="3":
    print("{} ile {} in çarpma {} dir.".format(a, b,a*b))
elif islem=="4":
    print("{} ile {} in bölme {} dir.".format(a, b,a/b))
else:
    print("Geçersiz işlem")








