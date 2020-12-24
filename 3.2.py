def function_2(name, surname, birth, city, email, phone):
    print(f"имя: {name}; фамилия: {surname}; дата рождения: {birth}; город: {city}; email: {email}; телефон: {phone}")


function_2(name = input("Введите имя"), surname = input("Введите фамилию"), birth = input("Введите дату рождения"),
           city = input("Введите город"), email = input("Введите email"), phone = input("Введите телефон"))
