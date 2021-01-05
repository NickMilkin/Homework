list1 = []
n = int(input('Введите количество элементов будущего списка'))
for i in range(n):
    list1.append(input())

for i in range(0, len(list1) - 1, 2):
    list1[i], list1[i + 1] = list1[i + 1], list1[i]
print(list1)
