def fact(n):
    if n == 0:
        yield f'Факториал нуля принят за единицу'
    i = 1
    for a in range(1, n + 1):
        i *= a
        yield f'Факториал числа {a} равен {i}'


for el in fact(int(input("Введите число"))):
    print(el)
