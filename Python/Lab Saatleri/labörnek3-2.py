def first():

 print("Çizilebilecek Şekiller: \n1) Dik Üçgen \n2) Eşkenar Üçgen \n3) Kare \n4) Dikdörtgen \n5) Daire ")

 count = int(input ("Kaç Şekil Çizmek İstiyorsunuz?: "))

 while count:
    number = input ("Çizmek istediğiniz şeklin kodunu giriniz: ")
    draw(number)
    count -= 1


def draw(number):


    if number == "1":

       rows = int(input("Dik üçgen için yükseklik değeri giriniz: "))
       for i in range(1,rows+1):
         print ("*"*i)


    elif number == "2":
        rows = int(input("Eşkenar üçgen için yükseklik değeri giriniz: "))
        for i in range(1,rows+1):
         print (" " * (rows - i) + "*" * (2*i - 1))


    elif number == "3":
        rows = int(input("Karenin bir kenar uzunluğu için değer giriniz: "))

        for i in range(1,rows+1):
          print ("*" * rows)


    elif number == "4":
        rows = int(input("Dikdörtgen için yükseklik değeri giriniz: "))
        columns = int(input("Dikdörtgen için genişlik değeri giriniz: "))
        for i in range(1,rows+1):
          print ("*" * columns)


    elif number == "5":
        rows = int(input("Daire için satır sayısını giriniz: "))

        for i in range(1,rows+1):
          if i <= rows/2:
             print (" " * (rows//2 - i+1) + "*" * (2*i - 1))

          else:
              print(" " * (i-rows//2-rows%2) + "*" * (2*(rows-i) +1) )

    else:
        print("Geçerli bir değer girmediniz!..")


first()
