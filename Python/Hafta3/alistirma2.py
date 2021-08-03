#Bu alıştırmada size iki kelimeden oluşan bir string(dize) veriliyor. Bu iki kelimenin değiştirildiği bir string(dize) döndürmeniz gerekir.

phrase = input("Cümle Giriniz: ")

def switch_words(phrase):

     blank = phrase.find(" ")

     first = phrase[:blank]
     second = phrase[blank+1:]

     return second + " " +first
    
print(switch_words(phrase))
