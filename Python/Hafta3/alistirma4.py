#Words.txt adlı dosyayı açın, dosyayı okuyun ve dosyanın içeriğini büyük harfle yazdırın. Çıktıyı üretmek için words.txt dosyasını kullanın.
filename = "words.txt"
fh = open(filename)
for line in fh:
    strip = line.rstrip()
    print(strip.upper())
