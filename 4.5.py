from functools import reduce


def func1(s_1, s_2):
    return s_1 * s_2


my_list = [n for n in range(100, 1001, 2)]
print(reduce(func1, my_list))
