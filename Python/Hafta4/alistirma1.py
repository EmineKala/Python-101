#romeo.txt dosyasını açın ve satır satır okuyun. Her satırı, split() fonksiyonunu kullanarak satırı bir String listesine bölün .
#Program bir kelime listesi oluşturmalıdır.
#Her satırdaki her kelime için, kelimenin zaten listede olup olmadığını kontrol edin ve eğer listedeyse tekrar eklemeyin.
#Program tamamlandığında, ortaya çıkan kelimeleri alfabetik sıraya göre sıralayın ve yazdırın.

list = list()
file = open( "romeo.txt")

for line in file:
 print(line.rstrip())
 words = (line.lower()). split()

 for word in words:
    
     if word not in list:
         list.append(word)


list.sort()
print(list)
