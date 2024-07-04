
# task 2 of the assignment
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

def calculate_average_grade(self, grades):
        if not grades:
            return 0.0
        return sum(grades) / len(grades)
