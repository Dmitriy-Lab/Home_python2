# Даны две строки. Посчитайте сколько раз каждый 
# символ первой строки встречается во второй

string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")
count = 0

for i in range(len(string1)):
    for x in range(len(string2)):
        if string1[i] == string2[x]:
            count += 1
        x += 1
    print(f"Элемент '{string1[i]}' первой строки встречается во второй {count} раз(a)")
    count = 0
    
