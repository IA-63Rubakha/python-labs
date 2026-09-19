def sort_by_date(data):
    return tuple(sorted(data, key=lambda x: (x[1][6:], x[1][3:5], x[1][0:2])))
students = (
    ["Петренко Іван", "12.05.2005"],
    ["Шевченко Оля", "03.11.2004"],
    ["Коваленко Максим", "25.01.2006"],
    ["Бондаренко Аня", "17.09.2005"]
)
print(sort_by_date(students))