print("""
*********************
KULLANICI GİRİŞİ
***********************
""")
sys_kullanıcı_adı="kubra"
sys_parola="123456"

kullanıcı_adı=input("Kullanıcı Adı:")
parola=input("Parola:")

if(kullanıcı_adı==sys_kullanıcı_adı and sys_parola!=parola):
    print("PAROLA HATALI...")

elif (kullanıcı_adı!=sys_kullanıcı_adı and parola == sys_parola):
    print("Kullanıcı ADI HATALI..")
elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
    print("KULLANICI ADI VE PAROLA HATALI...")
else:
    print("SİSTEME BAŞARIYLA GİRİŞ YAPILDI..")

