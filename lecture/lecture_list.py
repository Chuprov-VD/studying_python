# список
list_1 = []  # создание пустого списка
list_1 = list()  # создание пустого списка
print(list_1)
list_1 = [1, 3, 2, 6, 5, 4]
print(list_1)  # Выводит список как есть
print(*list_1)  # (*) перед переменной - выводит без скобочек и запятых
print("количество элементов: ", len(list_1))  # len() - выводит количество элементов
#   for i in list_1:    # цикл перебирает значения списка
#   print(i)
print("выводим элемент списка: ", list_1[0])  # - выводим 1 элемент списка
list_1.append(8)  # добавление нового элемента в конец списка
#   1. Удаление последнего элемента списка.
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop())  # 0
print(list_1)  # [12, 7, -1, 21]
print(list_1.pop())  # 21

#   2. Удаление конкретного элемента из списка.

list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0))  # 12
print(list_1)  # [7, -1, 21, 0]

#   3. Добавление элемента на нужную позицию.

list_1 = [12, 7, -1, 21, 0]
list_1.insert(2, 11)
print(list_1)  # [12, 7, 11, -1, 21, 0]

# Срез списка
# Отрицательное число в индексе — счёт с конца списка
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0])    # 1
print(list_1[1])    # 2
print(list_1[len(list_1)-1])    # 10