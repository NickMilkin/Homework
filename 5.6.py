file1 = open("text6.txt", "r", encoding="utf-8")
content = file1.readlines()
dict = {}
for i in content:
    i = i.replace("—", "").replace("(л)", "").replace("(пр)", "").replace("(лаб)", "").replace(".", "")
    dict[i.split()[0]] = sum(map(int, i.split()[1:]))
print(dict)
file1.closed()
