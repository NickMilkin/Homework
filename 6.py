a = int(input("Введите сколько спортсмен пробежал в первый день"))
b = int(input("Введите цель спортсмена"))
n = 1

while a<b:
    a *= 1.1
    n += 1
print(n)
