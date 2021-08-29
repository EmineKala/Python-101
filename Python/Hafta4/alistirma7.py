#mbox-short.txt dosyasını okumak için bir program yazın ve her mesaj için günün saatine göre dağılımı hesaplayın.
#Saati bularak ve ardından iki nokta üst üste kullanarak dizeyi ikinci kez bölerek saati ‘Başlangıç’ satırından çıkarabilirsiniz.
#Her saat için sayıları biriktirdikten sonra, aşağıda gösterildiği gibi saate göre sıralanmış sayımları yazdırın.
#Gönderen stephen.marquard@uct.ac.za Cmt 5 Ocak 09 : 14: 16 2008

file = open( "mbox-short.txt")

counts = dict()
list = []
for line in file:
    if not line.startswith("From "):
        continue
    words = line.split()[5:6]
    for word in words:
        counts[word] = counts.get(word,0)+1


for k,v in counts.items():
    list.append((k,v))

list.sort()
for k,v in list:                                    
    print(k,v)
