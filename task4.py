'''

Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
если известно, что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*
6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10
'''
num = int(input("Введите количество журавликов: "))
petr = num / 3 / 2
petr = int(petr)
sergei = petr
kate = (petr + sergei) * 2
print("Катя = {}\nПетя = {}\nСергей = {}".format(kate, petr, sergei))
