
def Ucgen(a,b,c):

    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
       print("Verilen Üçgen Dik Üçgendir.")

    elif a == b or a == c or b == c:
       print("Verilen Üçgen İkizkenar Üçgendir.")

    else:
       print("Verilen Üçgen İkizkenar ya da Dik Üçgen Değildir")



a = float(input("Üçgenin İlk Kenarı:"))
b = float(input("Üçgenin İkinci Kenarı:"))
c = float(input("Üçgenin Üçüncü Kenarı:"))

Ucgen(a,b,c)
