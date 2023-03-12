ogrenci_listesi = []

def ogrenci_ekle(ad,soyad):
    ogrenci_listesi.append(ad+" "+soyad)
    print(ad+" "+soyad+" eklendi.")
def ogrenci_cikar(ad,soyad):
    ogrenci_listesi.remove(f"{ad} {soyad}")
    print(ad + " " + soyad + " cikarildi.")
def ogrenciler_ekle(ogrenciler):
    ogrenci_listesi.extend(ogrenciler)
    for ogrenci in ogrenciler:
        print(ogrenci+" eklendi")
def ogrencileri_listele():
    print("ogrenci listesi:")
    for ogrenci in ogrenci_listesi:
        print(ogrenci)
def ogrenci_numarasi(ad,soyad):
    numara=ogrenci_listesi.index(ad+" "+soyad)
    print("{ad} {soyad}'in numarasi {numara}".format(ad=ad,soyad=soyad,numara=numara))
def ogrenciler_cikar(ogrenciler):
    i = 0
    while i< len(ogrenciler):
     ogrenci_listesi.remove(ogrenciler[i])
     print(ogrenciler[i] + " cikarildi")
     i+=1

print("----ogrenci ekle----")
ogrenci_ekle("ad1","soyad1")
ogrencileri_listele()
print("----ogrenci ekle----")
ogrenci_ekle("ad2","soyad2")
ogrencileri_listele()
print("----ogrenci cikar----")
ogrenci_cikar("ad1","soyad1")
ogrencileri_listele()
print("----ogrenciler ekle----")
ogrenciler_ekle(["ad3 soyad3","ad4 soyad4"])
ogrencileri_listele()
print("----ogrenci numarasi----")
ogrenci_numarasi("ad3","soyad3")
ogrencileri_listele()
print("----ogrenciler cikar----")
ogrenciler_cikar(["ad2 soyad2","ad3 soyad3"])
ogrencileri_listele()
