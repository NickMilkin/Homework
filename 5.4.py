file_old = open("text4.txt", "r", encoding="utf-8")
file_new = open("text4new.txt", "w", encoding="utf-8")
content = file_old.readlines()
translation = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
file_new.writelines([i.replace(i.split()[0], translation.get(i.split()[0])) for i in content])
file_new.close()
file_old.close()
