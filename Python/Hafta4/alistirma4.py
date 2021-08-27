#mbox-short.txt dosyasını okumak için bir program yazın ve en çok e-posta mesajını kimin gönderdiğini bulun .
#Program ‘From’ satırlarını arar ve bu satırların ikinci kelimesini postayı gönderen kişi olarak alır. Program, gönderenin posta adresini dosyada görünme sayısı ile eşleyen bir Python sözlüğü oluşturur.
#Sözlük oluşturulduktan sonra program, en üretken kaydediciyi bulmak için maksimum döngü kullanarak sözlükten okur.

file = open( "mbox-short.txt")

counts = dict()
for line in file:
    if not line.startswith("From "):
        continue
    words = line.split()[1:2]
    print(words)
    for word in words:
        counts[word] = counts.get(word,0)+1

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount=count
        bigword=word


print(bigword,bigcount)
