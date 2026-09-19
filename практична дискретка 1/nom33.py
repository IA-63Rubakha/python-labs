class Student:
    def __init__(self, name, courses, phone, email, degree):
        self.name = name
        self.courses = courses
        self.phone = phone
        self.email = email 
        self.degree = degree
    def printDetails(self): 
        print("Ім'я:", self.name)
        print("Курси:", self.courses) 
        print("Телефон:", self.phone)
        print("Email:", self.email) 
        print("Ступінь:", self.degree)
    def enroll(self, course): 
        self.courses.append(course)
s1 = Student("Марія", ["L548"], "+380501234567", "maria@mail.com", "Бакалавр") 
s1.enroll("Python")
s1.printDetails()


