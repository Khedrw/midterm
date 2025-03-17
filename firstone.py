class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        self.grade = grade
        super().__init__(name)

    def displayGrade(self):
        print(f"Student name: {self.name}, The grade: {self.grade}")
p = Student("Nabiha", 10)
p.displayGrade()