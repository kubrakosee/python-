print("""
***********************
kullanıcı girişi programı

***************************
""")
sys_kullanıcı_adı="kübra"
sys_parola="160622090"
giris_hakkı=3

while True: # Kullanıcı Doğru Giriş Yaptığında ve Giriş Hakkı bittiğinde sona erecek.
    kullanıcı_adı = input("Kullanıcı Adı:")
    parola = input("Parola:")

    if (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("Kullanıcı Adı Hatalı...")
        giris_hakkı -= 1
        print("Giriş Hakkı: ", giris_hakkı)
    elif (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("Parola Hatalı...")
        giris_hakkı -= 1

        print("Giriş Hakkı: ", giris_hakkı)
    elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("Kullanıcı Adı ve Parola Hatalı...")
        giris_hakkı -= 1
        print("Giriş Hakkı: ", giris_hakkı)

    else:
        print("Başarıyla Giriş Yaptınız...")
        break
    if (giris_hakkı == 0 ):

        print("Giriş Hakkınız Bitti...")
        break
