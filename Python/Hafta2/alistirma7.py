
#Bu alıştırmada, belirli sayıda satır verildiğinde
#bir yıldız üçgeni oluşturabilecek bir dize(string) döndürmelisiniz.


def star(rows):

    r = 0
    while r<= rows:
        print ("*"*r)
        r = r+1

rows = int(input("Satır sayısı giriniz: "))
star(rows)
