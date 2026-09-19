class Employee:
    def __init__(self, name, age, position, pay): 
         self.name = name
         self.age = age
         self.position = position
         self.pay = pay
    def show(self):
         print("Ім'я:", self.name)
         print("Вік:", self.age) 
         print("Посада:", self.position)
         print("Зарплата:", self.pay)
    def raise_pay(self, percent):
              self.pay += self.pay * percent / 100
    def is_adult(self):
              return self.age >= 18
e1 = Employee("Олег", 25, "Програміст", 30000)
e1.show()
e1.raise_pay(10)
print("Після підвищення:", e1.pay)
print("Повнолітній:", e1.is_adult())