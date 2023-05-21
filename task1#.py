'''
2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

*Пример:*

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''
import random
a = []
num = random.randint(1, 9) # генерируем список
for i in range(num): # добавляем в список новый элемент
    x = random.randint(1, 9)
    a.insert(i, x)
    result_list = []
print(a) # печатаем полученный список
quantity = len(a)
num = 1
if quantity % 2 == 0: # проверяем на четность для правильного произведения
    for i in range(quantity // 2):
        num = num + i
        result_list.insert(i, a[i] * a[-num])
else:
    for i in range(quantity // 2):
        num = num + i
        result_list.insert(i, a[i] * a[-num])
    result_list.insert(i + 1, a[quantity // 2] * a[quantity // 2]) # умножаем число само на себя так как нет пары
print(result_list)
