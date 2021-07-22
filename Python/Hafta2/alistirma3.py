#Çok sayıda insanı ve çok sayıda grubu alan bir fonksiyon yazın. Kişiler gruplara eşit olarak bölünecektir (fazla kişiler olabilir).
#Çift grupları oluşturduktan sonra kalan kişi sayısını döndürür.

def kalankisi(kisisayisi, grupsayisi):

    kalan = kisisayisi%grupsayisi
    return kalan

kisi = int(input("Kişi sayısını giriniz: "))
grup = int(input("Kaç grup olmalı: "))

print ("Dışarıda Kalan Kişi Sayısı:", (kalankisi(kisi, grup)))
