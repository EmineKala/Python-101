#Bir tamsayı listesi oluşturun ve bu listede tekrarlayan sayıları listeden kaldıran remove_duplicates adlı bir fonksiyon yazın.
#Misal:
#Girdi: remove_duplicates([2, 2, 1])
#Çıktı: [1,2]

list = ([1,2,5,4,8,7,8,7,9,9,0,4,3])
newlist = []

def remove_duplicates(list):
    
    for number in list:
        if number not in newlist:
            newlist.append(number)
            newlist.sort()

    return newlist


print(remove_duplicates(list))
