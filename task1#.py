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
    result_list.insert(i, a[quantity // 2] * a[quantity // 2]) # умножаем число само на себя так как нет пары
print(result_list)