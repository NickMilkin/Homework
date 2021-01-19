import json
profitable = []
with open("ex7.json", "w", encoding="utf-8") as json_file:
    with open("text7.txt", "r", encoding="utf-8") as read_file:
        dict = {i.split()[0]: int(i.split()[2]) - int(i.split()[3]) for i in read_file}
        for a in dict.values():
            if a > 0:
                profitable.append(a)
        json.dump(dict, json_file, ensure_ascii=False, indent=4)
        res = sum(profitable) / len(profitable)
        json.dump(res, json_file, ensure_ascii=False, indent=4)
