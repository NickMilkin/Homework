n = int(input('Введите порядковый номер месяца'))
list1 = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
print(f'Время года - {list1[n-1]}')
dict1 = {1: "Зима", 2: "Весна", 3: "Лето", 4: "Осень", 5: "Зима"}
print(f"Время года - {dict1[n // 3 + 1]}")
