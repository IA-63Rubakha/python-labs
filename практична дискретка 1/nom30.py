months = ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень",
          "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"]
winter = tuple(months[0:2] + months[11:12])
spring = tuple(months[2:5])
summer = tuple(months[5:8])
autumn = tuple(months[8:11])
result = (winter, spring, summer, autumn)
print(result)