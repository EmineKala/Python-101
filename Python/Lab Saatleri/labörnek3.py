
def first():

 print("Çizilebilecek Şekiller: \n1) Dik Üçgen \n2) Eşkenar Üçgen \n3) Kare \n4) Dikdörtgen \n5) Daire ")

 count = int(input ("Kaç Şekil Çizmek İstiyorsunuz?: "))

 while count:
    number = input ("Çizmek istediğiniz şeklin kodunu giriniz: ")
    draw(number)
    count -= 1


def draw(number):
    r=0

    if number == "1":

       rows = int(input("Dik üçgen için yükseklik değeri giriniz: "))
       while r <= rows:
         print ("*"*r)
         r = r+1

    elif number == "2":
        rows = int(input("Eşkenar üçgen için yükseklik değeri giriniz: "))
        while r <= rows:
         print ("   " * (rows - r) + " * " * (2*r - 1))
         r = r+1

    elif number == "3":
        rows = int(input("Karenin bir kenar uzunluğu için değer giriniz: "))
        print()
        while r < rows:
          print (" * " * rows)
          r = r+1

    elif number == "4":
        rows = int(input("Dikdörtgen için yükseklik değeri giriniz: "))
        columns = int(input("Dikdörtgen için genişlik değeri giriniz: "))
        while r < rows:
          print (" * " * columns)
          r = r+1

    elif number == "5":
        rows = int(input("Daire için satır sayısını giriniz: "))
        while r < rows:

             print (":(")

             r = r+1

    else:
        print("Geçerli bir değer girmediniz!..")


first()
