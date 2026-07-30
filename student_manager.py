class Student:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)


name = input("Enter student name: ")
age = int(input("Enter student age: "))

student = Student(name, age)

student.introduce()