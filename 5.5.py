file1 = open("text5.txt", "w+", encoding="utf-8")
input_list = input().split()
file1.writelines(" ".join(input_list))
input_list = map(int, input_list)
print(sum(input_list))
file1.closed()
