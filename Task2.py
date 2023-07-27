from random import randint as rd
n = int(input("Введите количество кустов: "))
list_1 = list()
for i in range(n):
    list_1.append(rd(1, 100))
    max = 0
    sum = 0
    temp = 0
print(list_1)
for j in range(n):
    sum = list_1[j] + list_1[j + 1] + list_1[j + 2]
    list_1.append(list_1[j])
    if sum > max:
        max = sum
print(f'Максимальное число ягод, которые может собрать за один заход собирающий модуль = {max}')