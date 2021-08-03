#Size bir dosya adı soran, ardından bu dosyayı açan ve dosyanın satırlarını arayarak dosya içini okuyan bir kod verildi.
#Sizden istediğimiz, "X-DSPAM-Confidence: " değerlerinin ortalamasını bulmanız. Örnek bir satır:

#X-DSPAM-Confidence: 0,8475
#Ardından aşağıda gösterildiği gibi bir çıktı oluşturun. Çözümünüzde sum() fonksiyonunu veya sum adlı bir değişken kullanmayın.

#İstenilen Çıktı:

#Ortalama X-DSPAM-Confidence: 0,7507185185185187


fname = "mbox-short.txt"
fh = open(fname)
x=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
      continue
    print(line)

    count = count+1

    con = line.find(" ")

    piece = line[con+1:]

    x = x + float(piece)

print("Ortalama: ", x/count)


print("Done")
