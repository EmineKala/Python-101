#Kullanıcı 'done' ifadesini girene kadar bir kullanıcıdan sürekli olarak tamsayı sayıları isteyen bir program yazın. 'done' girildikten sonra, sayıların en büyük ve en küçüğünü yazdırın.
#Kullanıcı geçerli bir numaradan başka bir şey girerse, onu bir try/except yardımı ile yakalayın ve uygun bir mesaj yazdırın. 

largest = None
smallest = None

while True:

    num = input("Lütfen Bir Tamsayı Değeri Giriniz: ")

    if num == "done" :
       break

    try:
        number = int(num)
    except:
        print("Geçersiz bir değer girdiniz!")
        continue

    if largest is None:
       largest = number
    elif number > largest:
       largest = number
    if smallest is None:
       smallest = number
    elif number < smallest:
       smallest = number


print("En Büyük Sayı:", largest)
print("En Küçük Sayı:", smallest)
