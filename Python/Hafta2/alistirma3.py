#Çok sayıda insanı ve çok sayıda grubu alan bir fonksiyon yazın. Kişiler gruplara eşit olarak bölünecektir (fazla kişiler olabilir).
#Çift grupları oluşturduktan sonra kalan kişi sayısını döndürür.

def kalankisi(kisisayisi, grupsayisi):

    if grup*2 >= kisi and kisisayisi%2 == 1 :
       kalan = 1


    elif grup*2 >= kisi and kisisayisi%2 == 0:
       kalan = 0

    else:
       kalan = kisi - grup*2

    return kalan

kisi = int(input("Kişi sayısını giriniz: "))
grup = int(input("Kaç grup olmalı: "))

kalan = kalankisi(kisi, grup)
print ("Dışarıda kalan kişi sayısı:" , kalan)
