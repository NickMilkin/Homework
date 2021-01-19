from itertools import count, cycle

# a)
a = int(input('Сколько чисел генерировать?'))
n = int(input('С какого начинать?'))
i = 0
for n in count(n):
    if i == a:
        break
    print(n)
    i += 1

# б)
my_list = input('Введите список, разделяя элементы пробелом').split()
a = int(input('Сколько раз вывести?'))
i = 0

generate = cycle(my_list)

for i in range(a):
    print(next(generate))
