# EXE 1
# """names = ["Dominion", "John", "Mary"]
# my_iter = iter(names)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))"""

#EXE2

def count_to_five():
    yield 1
    yield 2 
    yield 3 
    yield 4
    yield 5
for n in count_to_five():
    print(n)

# exe 3

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Dominion", 20)
student2 = Student("John", 21)
student3 = Student("Mary", 19)
students = [student1, student2, student3]
def student_generator(students):
    for student in students:
        yield student
for student in student_generator(students):
    print(student.name)