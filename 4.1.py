import sys


def my_func():
    try:
        hours, salary, add = map(int, sys.argv[1:])  # Ввод данных через терминал
        print(hours * salary + add)
    except ValueError:
        print('В введенных данных есть ошибка')


my_func()
