# 1 задача.
# Создайте список из случайных чисел.
# Найдите номер его последнего локального максимума (локальный максимум — это элемент,
# который больше любого из своих соседей).
# 2 задача
# Создайте список из случайных чисел.
# Найдите максимальное количество его одинаковых элементов.
# 3 задача.
# Создайте список из случайных чисел. Найдите второй максимум.
#
# a = [1, 2, 3] # Первый максимум == 3, второй == 2
# 4 задача.
# Создайте список из случайных чисел. Найдите количество различных элементов в нем.


import random

random_len = []
n = int(input("Введите размер списка: "))
number = 0


def random_num(num, random_len_fun):
    x = random.randint(1, 9)
    random_len.append(x)
    num -= 1
    if num > 0:
        return random_num(num, random_len_fun)
    else:
        return random_len


def replay(num, random_len):
    count_max = 0
    j = 0
    count = 1
    for i in random_len:
        j += 1
        if j < len(random_len) and i == random_len[j]:
            count += 1
        elif count_max < count:
            count_max = count
            num = i
            count = 1
        else:
            count = 1
    print(f"Больше всего {num}, встречалось: {count_max} раз")
    return num, count_max


def second_max(random_len_maxnum2):
    j = random_len_maxnum2[len(random_len_maxnum2) - 1]
    for i in range(len(random_len_maxnum2) - 1, 0, -1):
        if random_len_maxnum2[i] != j:
            return random_len_maxnum2[i]


def different(list_random):
    j = list_random[len(list_random) - 2]
    different_list = [list_random[1]]
    for i in list_random:
        if different_list[len(different_list) - 1] != i:
            different_list.append(i)
    print(different_list)
    return


print(random_num(n, random_len))  # вывод сгенерированного списка
print(f"Первое максимальное число равно: {sorted(random_len)[n - 1]}")  # 1 Задача
random_len = sorted(random_len)  # сортировка списка
print(random_len)
replay(number, random_len[-1::-1])  # 2 Задача
print(f"Второе максимальное число равно: {second_max(random_len)}")  # 3 задача
print(f"Список без дубликатов: ")
different(random_len)  # 4 задача
