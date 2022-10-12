# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.

num = int(input("Введите N: "))
list = []
for i in range(-num, num + 1):
    list.append(i)
list = list[-2:]+list[:-2]
print(list)