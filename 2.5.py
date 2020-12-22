rating = [10, 7, 4, 2, 1]
while True:
    print(f"Текущий рейтинг: {rating}")
    n = input('Введите новое натуральное число. Если хотите остановиться, введите СТОП')
    if n != "СТОП":
        rating.append(int(n))
        rating = sorted(rating, reverse = True)
    else: break
