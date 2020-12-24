def function_1(d1, d2):
    try:
        print(round(d1 / d2, 2))
    except ZeroDivisionError:
        print("На ноль делить нельзя")


function_1(int(input("Введите делимое")), int(input("Введите делитель")))
