#Tüm kullanıcı adlarını ve şifreleri takip eden users  adında sözlüğe dayanarak bir kullanıcı adı ve şifrenin doğru olup olmadığını kontrol eden bir fonksiyon yazın.
#Fonksiyonunuz, verilen kullanıcı adı ve şifrenin doğru olup olmadığına bağlı olarak True veya False dönmelidir.

users = dict()
users["eminekala"] = "1234"
username = input("Kullanıcı adı:")
password = input("Şifre:")

def check_login(username, password):

    if username in users.keys() and users[username] == password:
        return True
    else:
        return False

print(check_login(username, password))
