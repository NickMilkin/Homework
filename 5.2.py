my_text = open("text2.txt", "r", encoding="utf-8")
content = my_text.readlines()
for id, item in enumerate(content):
    words = len(item.split())
    print(f"Строка номер {id + 1} содержит {words} слов")
my_text.close()
