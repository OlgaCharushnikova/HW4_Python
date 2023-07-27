from random import randint as rd
n = int(input("Введите количество элементов множества 1: "))
m = int(input("Введите количество элементов множества 2: "))
list_1 = list()
list_2 = list()
list_3 = set()
for i in range(n):
    list_1.append(rd(1, 10))
print(list_1)
for i in range(m):
    list_2.append(rd(1, 10))
print(list_2)
list_1 = set(list_1)
list_2 = set(list_2)
list_3 = list_1.intersection(list_2)
list_3 = list(list_3)
print(list_3)


                    



