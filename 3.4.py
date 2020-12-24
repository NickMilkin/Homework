def my_func(x, y):
        y = abs(y)
        answer = x
        for i in range(1, y):
            answer *= x
        answer = 1 / answer
        return answer


try:
    s1 = int(input("Введдите положительное число"))
    s2 = int(input('Введите отрицательное число'))
    if s1 <= 0 or s2 >= 0:
        print("Вы ввели неправильные данные")
    else:
        print(my_func(s1, s2))
except ValueError:
    print("Вы ввели неправильные данные")