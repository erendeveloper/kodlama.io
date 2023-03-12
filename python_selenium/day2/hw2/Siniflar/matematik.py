class Matematik:
    def __init__(self,sayi1,sayi2): #constructor yapici
        self.s1=sayi1
        self.s2=sayi2
        print("Matematik basladi (referansi olustu)")
    def topla(self):
        return self.s1+self.s2
    def cikar(self):
        return self.s1-self.s2
    def bol(self,sayi1):
        return self.s1/self.s2
    def carp(self):
        return self.s1*self.s2

matematik = Matematik(6,7)
sonuc=matematik.topla()
print("sonuc:"+str(sonuc))
print(matematik.sayi3)

class Istatistik(Matematik)
    def __init__(self,sayi1,sayi2):
        super().__init__(sayi1,sayi2)
    def varyansHesapla(self):
        return self.s1*self.s2

istatistik = Istatistik(5,8)
istatistik.