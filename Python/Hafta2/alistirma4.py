#İlk hız, ivme ve zaman verildiğinde, son hızı döndürecek bir fonksiyon yazın.

def sonhiz (vi, a, t):

    vf = vi + a*t
    return vf

ilkhiz = int(input("İlk hızı giriniz: "))
ivme =  int(input("İvmeyi giriniz: "))
zaman = int(input("Zamanı giriniz: "))

print("Son Hız: " , (sonhiz(ilkhiz,ivme,zaman)))
