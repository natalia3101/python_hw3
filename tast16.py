# Задача 16: Требуется вычислить, сколько раз 
# встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1

from random import randint
list_1 = [randint(1, 20) for i in range(5)]

n = int(input("Enter a number from 1 to 20: "))
count = 0
for i in range(len(list_1)):
    if n == list_1[i]:
        count += 1

print(list_1)
print(count)