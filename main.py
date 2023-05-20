# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
# Решение 1:
num = input("Введите число: ")
result = int(num[0]) + int(num[1]) + int(num[2])
print(num, "-> {} ({} + {} + {})".format(result, num[0], num[1], num[2]))

# Решение 2:
num = int(input("Введите число: "))
inter_num = 0
while num > 0:
    n = num % 10
    inter_num = inter_num + n
    num = num // 10
print(inter_num)

# Решение 3:
num = input("Введите число: ")
while len(num) != 3:
    num = input("Введите 3-х значное число")
num1 = 0
for i in num:
    num1 = int(i) + num1
print(num1)
