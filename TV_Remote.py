import random
import time

class Kumanda():
    def __init__(self,tv_durum="Kapali",tv_ses=0,kanal_listesi=["TRT"],kanal="TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def sesi_azalt_artir(self):
        while True:
            karakter = input("Sesi azaltmak icin '<' artirmak icin '>' cikis icin 'q' basiniz...")
            if (karakter == "<"):
                if (self.tv_ses !=0):
                    self.tv_ses -= 1
                    print("Ses : ",self.tv_ses)
            elif (karakter == ">"):
                if (self.tv_ses !=30):
                    self.tv_ses += 1
                    print("Ses : ",self.tv_ses)
            else:
                print("Ses guncellendi...")
                break

    def tv_kapat(self):
        print("Tv Kapatiliyor")
        self.tv_durum = "Kapali"

    def tv_ac(self):
        print("Tv Aciliyor")
        self.tv_durum = "Acik"

    def __str__(self):
        return "TV Durumu : {}\nTV Ses : {}\nKanallar : {}\nSuanki Kanal : {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def rastgele_kanal(self):
        rastgele = random(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Suanki Kanal : ",self.kanal)

    def kanal_ekle(self,kanal):
        self.kanal_listesi.append(kanal)
        print("Kanal Eklendi ",kanal)

kumanda = Kumanda()
print("""
*******************************************
        Televizyon Uygulamasi
        
Islemler
--------

1. Televizyonu Ac

2. Televizyonu Kapat

3. Televizyon Bilgileri

4. Kanal Sayisini Ogren

5. Kanal Ekle

6. Rastgele Kanala Gec

7. Sesi Azalt yada Artir

Cikmak icin 'q' ya basiniz      
""")

while True:
    islem = input("Isleminizi Seciniz : ")
    if (islem == "q"):
        print("Programdan Cikiliyor")
        break
    if (islem == "1"):
        kumanda.tv_ac()
    elif (islem == "2"):
        kumanda.tv_kapat()
    elif (islem == "3"):
        print(kumanda)
    elif (islem == "4"):
        len(kumanda)
    elif (islem == "5"):
        kanallar = input("Eklemek istediginiz kanallari ',' ile ayirarak giriniz : ")
        eklenecekler = kanallar.split(",")
        for i in eklenecekler:
            kumanda.kanal_ekle(i)
        print("Kanal Listesi Basariyla Guncellendi...")
    elif (islem == "6"):
        kumanda.rastgele_kanal()
    elif (islem == "7"):
        kumanda.sesi_azalt_artir()
    else:
        print("Gecersiz Islem")



