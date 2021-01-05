words = input('Введите слова, разделенные пробелами').split(" ")
for i in range(len(words)):
    print(f'{i+1}) {words[i][:10]}')