'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали
билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых
трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к.
3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no
'''

num = input("Введите номер билета: ")
while len(num) != 6:
    num = input("Введите номер шестизначного билета: ")
num1 = num[:3]
num2 = num[3:]
left_num = 0
right_num = 0
for i in num1:
    left_num = int(i) + left_num
for i in num2:
    right_num = int(i) + right_num
equality = left_num - right_num
if equality == 0:
    print("yes")
else:
    print("no")
