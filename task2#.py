'''
1 Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка,
стоящих на нечётной позиции.
*Пример:*

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
# для нечетных позиций
import random

a = []
num = random.randint(1, 9)
for i in range(num):
    x = random.randint(1, 9)
    a.insert(i, x)
print(a)
num = 0
quantity = len(a)
for i in range(quantity):
    if i % 2 != 0:
        num = num + a[i]
print("Сумма чисел на нечетном индексе =", num)
# для нечетных чисел
num = 0
for i in a:
    if i % 2 != 0:
        num = num + i
print("Сумма нечетных чисел =", num)
