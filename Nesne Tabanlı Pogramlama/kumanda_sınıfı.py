import random
import time

class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["Trt"],kanal="Trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
        
    def tv_ac(self):
        if(self.tv_durum == "Açık"):
            print("Televizyon Zaten Açık....")
        else:
            print("Televizyon Açılıyor...")
            self.tv_durum="Açık"
            
    def tv_kapalı(self):
        if(self.tv_durum == "Kapalı"):
            print("Televizyon Zaten Kapalı")
        else:
            print("Televizyon Kapanıyor...")
            self.tv_durum="Kapalı"

    def ses_ayarları(self):
        while True:
            cevap=input("Sesi Azalt:'<'\nSesi Artır:'>'\nÇıkış:çıkış")
            if(cevap =="<"):
                if(self.tv_ses!=0):
                    self.tv_ses -=1
                    print("Ses:", self.tv_ses)
            elif(cevap ==">"):
                if(self.tv_ses != 31):
                        self.tv_ses +=1
                        print("Ses:",self.tv_ses)
            else:
                print("Ses Güncellendi:",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)
        print("Kanal Eklendi....")

    def rastgele_kanal(self):

        rastgele=random.randint(0,len(self.kanal_listesi)-1)

        self.kanal=self.kanal_listesi[rastgele]

        print("Şu Anki Kanal:",self.kanal)

    def __len__(self):

        return  len(self.kanal_listesi)

    def __str__(self):

        return "TV Durumu:{}\n TV Ses:{}\nKanal Listesi:{}\nŞu Anki Kanal:{}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda = Kumanda()

print("""
Televizyon Uygulaması

1.Tv Aç

2.Tv Kapat

3.Ses Ayarları

4.Kanal Ekleme

5.Kanal Sayısını Öğrenme

6.Rastgele Kanala Geçme

7.Televizyon Bilgileri

Çıkmak için 'q'ya basın


""")

while True:

    İşlem=input("İşlemi Seçiniz:")

    if(İşlem == "q"):

        print("Program Sonlandırılıyor....")

        break

    elif(İşlem=="1"):

        kumanda.tv_ac()

    elif(İşlem=="2"):

        kumanda.tv_kapalı()

    elif(İşlem=="3"):

        kumanda.ses_ayarları()

    elif(İşlem=="4"):

        kanal_isimleri=input("Kanal İsimleri ', 'ile ayırarak girin:")

        kanal_listesi=kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:

            kumanda.kanal_ekle(eklenecekler)

    elif(İşlem=="5"):

        print("Kanal Sayısı:",len(kumanda))

    elif(İşlem=="6"):

        kumanda.rastgele_kanal()

    elif(İşlem=="7"):

        print(kumanda)
    else:
        print("Geçersiz İşlem....")


