file1 = open("text3.txt", "r", encoding="utf-8")
content = file1.readlines()
dict = {i.split()[0]: int(i.split()[1]) for i in content}
low = [s[0] for s in dict.items() if s[1] < 20000]
print(f"{low}. Средний доход: {sum(dict.values()) / len(dict)}")
file1.close()
