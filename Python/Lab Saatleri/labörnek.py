isim = input("Adınızı Giriniz: ")
yas = int(input("Yaşınızı Giriniz: "))
ortalama = float(input("Not Ortalamanızı Giriniz: "))

if yas>=17 and yas<=21:
    if ortalama>=80:
       print("Tebrikler!.. Okulu başarıyla tamamladınız:)")
    else:
       print("Üzgünüz, okulu tamamlayamadınız:(")
else:
   print("Öğrenci yaşı okul için uygun değil")
