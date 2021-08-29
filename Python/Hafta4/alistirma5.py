#İki listeyi bir sözlüğe eşleyen ve yeni sözlüğü döndüren bir işlev yazın.
#Misal:
#list1 = [1, 2, 3]
#list2 = [8, 9, 10]
#new_dictionary = {1:8 , 2:9 , 3:10}

list1 = [1,2,3]
list2 = [4,5,6]
i=0
new_dictionary = dict()

for k in list1:
    new_dictionary[k] = list2[i]
    i = i+1


print("new_dictionary=" ,new_dictionary)
