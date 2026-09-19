first_name = input("Введи ім'я: ")
last_name = input("Введи прізвище: ")
phone = input("Введи телефон: ")
if not first_name or not last_name or not phone:
    print("Не залишайте жодні поля порожніми")
else:
    print("Спасибі")
if first_name or last_name or phone:
    print("Спасибі")
else:
    print("Не залишайте всі поля порожніми")
if not first_name or not last_name:
    print("Не залишайте жодні поля порожніми")
else:
    print("Спасибі")