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
        return "TV Durumu : {}\nTV Ses : {}\nKanallar : {}\nSuanki Kanal : {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal

    def __len__(self):
        return len(self.kanal_listesi)

    

