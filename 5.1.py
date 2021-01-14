with open(r"text_1.txt", "w", encoding="utf-8") as file1:
    while True:
        data = input('Введите строку, чтобы закончить, введите пустую строку')
        if not data:
            break
        else:
            print(data, file=file1)
