#0.0 ile 1.0 arasında bir puan istemek için bir program yazın. Puan aralık dışındaysa bir hata yazdırın. Puan 0,0 ile 1,0 arasında ise, aşağıdaki tabloyu kullanarak bir harf notu yazdırın:
#Puan		Not
#> = 0,9		A
#> = 0,8		B
#> = 0,7 	C
#> = 0,6 	D
#<0,6 		F
#Kullanıcı aralık dışında bir değer girerse, uygun hata mesajı ve çıkış( quit() ) yapın.

puan = input("Puan: ")

try:
    p = float(puan)

except:
    p = -1
    print("Yanlış değer girdiniz!..")
    quit()

if 0.0 <= p <= 1.0:
       if p >= 0.9:
          print("A")
       elif p >= 0.8:
          print("B")
       elif p >= 0.7:
          print("C")
       elif p>= 0.6:
          print("D")
       else:
          print("F")
else:
    print("Girilen değer aralıkta değil!..")
    quit()
