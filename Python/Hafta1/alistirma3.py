#Brüt ücreti hesaplamak için input() kullanarak kullanıcıdan saat başına ücret ve saati isteyen bir program yazın.
#Programı test etmek için 35 saat ve saat başına ücret olarak 2,75 TL kullanın (ücret 96,25 TL olmalıdır).
#Bir stringi okumak için input() ve stringi bir sayıya dönüştürmek için float () fonksiyonlarını kullanmalısınız.
#Kullanıcının kesinlikle sayısal bir değer girecektir.

saat = float(input("Saat giriniz:"))
ücret = float(input("Saat başına ücret:"))
brüt = saat*ücret

print("Brüt", brüt)
