try:
    my_list = [int(n) for n in input('Введите список, разделяя элементы пробелом').split()]
    new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
    print(new_list)
except ValueError:
    print('Ошибка в введенных данных')
