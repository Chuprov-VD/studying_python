"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""


def degree(a, b, c):
    b = b - 1
    if b > 0:
        a = a * c
        return degree(a, b, c)
    return a


a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = a
res = degree(a, b, c)
print(res)