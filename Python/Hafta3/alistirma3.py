#Bu egzersizde size 3 kelimelik bir dizi ve bu üç kelimeden birine karşılık gelen bir sayı verilecek.
# Verilen sayı sırasındaki kelimeyi iki kez yazdıran bir fonksiyon yazın.

phrase = "domates biber patlıcan"
ref = input("Kaçıncı kelime tekrar etsin: ")

def double_word(phrase, ref):

     blankone = phrase.find(" ")

     first = phrase[:blankone]

     piece = phrase[blankone+1: ]

     blanktwo = piece.find(" ")

     second = piece[:blanktwo]

     third = piece [blanktwo+1: ]

     if ref == "1":

       first = first + " " + first

     elif ref == "2":

       second = second + " " + second

     else:
        third = third + " " + third
     return first + " " + second + " " + third


print(double_word(phrase, ref))
