# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
my_list = [random.randint(0, 100) for _ in range(10)]
print(my_list)
min = int(input("Введите минимум: "))
max = int(input("Введите максимум: "))

for i in range(len(my_list)):
    if min <= my_list[i] <= max:
        print(i)