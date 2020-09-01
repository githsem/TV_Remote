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
                    
