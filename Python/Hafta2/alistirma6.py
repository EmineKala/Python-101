#Bu egzersizde, size bir alışveriş listesi ve bir eşya verilecek.
#Eğer verilen eşya alışveriş listesinde ise True döndürün, alışveriş listesinde değilse False döndürün.

def shopping_list(list,item):

    found = False
    for i in list:
      if i == item:
         found = True

    return found

list = ["süt","yumurta","ekmek","peynir", "zeytin"]
item = input ("Listede aranacak değeri yazınız:")

print(shopping_list(list,item))
