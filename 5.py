profit = int(input("Введите прибыль фирмы"))
costs = int(input("Введите издержки фирмы"))

if profit == costs:
    print("Фирма работает в ноль")
elif profit < costs:
    print("Фирма работает в убыток")
elif profit > costs:
    print("Фирма работает с прибылью")
    workers = int(input("Введите количество сотрудников"))
    print(f'Рентабельность = {profit / costs * 100:.2f}%; Прибыль на одного сотрудника = {profit / workers:.2f}')
