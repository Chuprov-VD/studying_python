#   Кортеж — это неизменяемый список.

t = ()  # создание пустого кортежа
print(type(t))  # class <'tuple'>
t = (1,)  # для создания кортежа с одним эдементом нужно добавить (,) иначе будет считаться как обычное число
print(type(t))
t = (28, 9, 1990)
print(type(t))
colors = ['red', 'green', 'blue']
print(colors)  # ['red', 'green', 'blue']
t = tuple(colors)  # присваеваем списку звание класс кортежж
print(t)  # ('red', 'green', 'blue')
t = tuple(['red', 'green', 'blue'])
print(t[0])  # red
print(t[2])  # blue
for e in t:
    print(e)  # red green blue

#   t[0] = 'black' # TypeError: 'tuple' object does not support(нельзя изменять кортеж)
#   распаковка кортежей в независимые переменные
t = tuple(['red', 'green', 'blue', 1])
green, red, blue, one = t    # они присваиваються по порядку, необходимо что бы кол-во переменных и размер кортежа
# сходились
print('r:{} g:{} b:{}'.format(red, green, one))  # r:red g:green b:blue
