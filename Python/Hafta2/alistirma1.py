
#Brüt ücreti hesaplamak için input() fonksiyonunu kullanarak kullanıcıdan çalışma saati girdisini alın. Buradan sonra ödeme hesaplaması mantığı için computePay() adlı bir fonksiyon oluşturup işlemler için bu fonksiyonu kullanın. Çalışma saati 40 ve altındaysa saat başına ücret 10 TL'dir. 
#40 saatin üstünde çalışıldıysa saat başına ücret 15 lira sayılmaktadır. Girilen saate göre ücreti hesaplayan, sizin tarafınızdan oluşturulan fonksiyon ile çalışan bir kod yazınız.
#Test etmek için 30 saat değerini giriniz, sonuç 300 TL çıkmalı, ikincil test olarak 50 değerini giriniz, sonuç 750 TL çıkmalı.


def computePay():

    if saat <=40:
       ucret = saat * 10
    else:
        ucret = saat * 15

    print("Brüt Ücret: " ,ucret)
    return

saat = int(input("Saat giriniz: "))
computePay()
