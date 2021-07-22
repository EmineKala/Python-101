#Brüt ücreti hesaplamak için input() kullanarak kullanıcıdan çalışma saati alın. 40 saate kadar, her saat başına ücret 10 TL dir. 40 saatin üstündeki saatlerin ücreti 15 TL olmaktadır. Girilen saate göre ücreti hesaplayan bir kod yazınız.

#Test etmek için 30 saat değerini giriniz, sonuç 300 TL çıkmalı, ikincil test olarak 50 değerini giriniz, sonuç 550 TL çıkmalı.

saat = input("Çalışma saati:")
s = float(saat)

if s<=40:
   brüt = s*10
else:
   ek = s - 40
   brüt = 40*10 + ek*15

print("Brüt Ücret:" , brüt )
