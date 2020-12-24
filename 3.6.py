def int_func():
    _str = input("Введите строку слов, написанных латинскими буквами нижнего регистра, разделенные пробелами").split()
    for i in _str:
        print(i.title())


int_func()
