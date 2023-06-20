"""
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также
может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
"""

file = r"guide.txt"     # безопасное чтение адреса файла(относительно python файла)
name = input("Вы хотите добавить имя или фамилию? Если да пишите Yes: ").upper()
with open(file, "a") as file_r:     # безопасное открытие файла, и передача его в переменную
    while name == "YES":
        name = input("Введите имя для записи: ")
        file_r.write("\n" + name)
        surname = input("Введите фамилию для записи: ")
        file_r.write(" " + surname)
        num = input("Введите номер телефона: ")
        file_r.write(" " + num)
        surname = input("Вы хотите добавить другую фамилию или имя? Если да пишите Yes").upper()

name_rem = input("Вы хотите заменить имя? Если да пишите Yes: ").upper()
surname_rem = input("Вы хотите заменить фамилию? Если да пишите Yes: ").upper()
num_rem = input("Вы хотите заменить номер? Если да пишите Yes: ").upper()

with open(file) as file_r:
    while (name_rem or surname_rem) == "YES":
        if name_rem == "YES":
            name_rem = input("Введите имя для удаления: ")
            name = input("Введите имя для записи: ")
            file_r = file_r.read().replace(name_rem, name).strip()  # удаляет выбранные символы и заменяет на
            # переменную
            name_rem = input("Вы хотите заменить другое имя? Если да пишите Yes").upper()
        elif surname_rem == "YES":
            surname_rem = input("Введите фамилию для удаления: ")
            surname = input("Введите фамилию для записи: ")
            file_r = file_r.read().replace(surname_rem, surname).strip()  # удаляет выбранные символы и заменяет на
        elif num_rem == "YES":
            num_rem = input("Введите номер для удаления: ")
            num = input("Введите номер для записи: ")
            file_r = file_r.read().replace(num_rem, num).strip()

        # переменную
            surname_rem = input("Вы хотите заменить другую фамилию? Если да пишите Yes").upper()
    new_guide = open(file, "w")
    new_guide.write(file_r)
    new_guide.close()
