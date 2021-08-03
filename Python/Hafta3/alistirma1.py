#Aşağıdaki satırın sonundaki sayıyı çıkarmak için find () ve dizi dilimlemeyi (bkz. Bölüm 6.10) kullanarak kod yazın.
#Çıkarılan değeri kayan noktalı sayıya dönüştürün ve yazdırın.

text = "X-DSPAM-Confidence:    0.8475";
a = text.find(":")
piece = text[a+1:]

print(float(piece))
