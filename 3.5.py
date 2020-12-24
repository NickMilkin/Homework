def user_sum():
    _sum = 0
    while True:
        user_list = input("Введите числа, разделяя их пробелом. Чтобы выйти, введите R").split(" ")
        for i in user_list:
            if i == "R":
                return _sum
            else:
                _sum += int(i)
        print(f"Сумма равна {_sum}")


print(user_sum())