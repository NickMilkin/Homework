features = {"название": "", "цена": "", "количество": "", "ед": ""}
analysis = {"название": [], "цена": [], "количество": [], "ед": []}
n = 0
while True:
    n += 1
    name = input('Введите название товара, если хотите завершить, введите СТОП')
    if name == "СТОП":
        break
    features['название'] = name
    analysis['название'].append(features['название'])
    price = input('Введите цену товара')
    features['цена'] = int(price)
    analysis['цена'].append(features['цена'])
    number = input('Введите количество товара')
    features['количество'] = int(number)
    analysis['количество'].append(features['количество'])
    unit = input('Введите единицу измерения товара')
    features['ед'] = unit
    analysis['ед'].append(features['ед'])
    print(f"{n}) {features}")
print(analysis)


