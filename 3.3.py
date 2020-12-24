def my_func(n1, n2, n3):
    a = [n1, n2, n3]
    a.remove(min(a))
    return sum(a)


print(my_func(int(input("Введите число")), int(input("Введите число")), int(input("Введите число"))))