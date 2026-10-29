
students = []


class Student:
    def __init__(self, name, age, course, email):
        self.name = name
        self.age = age
        self.course = course
        self.email = email

    def introduce(self):
        return (
            f"Welcome {self.name}, your details are stored here.\n"
            f"Details (name: {self.name}, age: {self.age},\n"
            f"study course: {self.course}, email: {self.email})"
        )


class GraduateStudent(Student):
    def __init__(self, name, age, course, email, thesis_topic):
        super().__init__(name, age, course, email)
        self.thesis_topic = thesis_topic

    def introduce(self):
        return (
            f"Welcome {self.name}, your details are stored here.\n"
            f"Details (name: {self.name}, age: {self.age},\n"
            f"study course: {self.course}, email: {self.email})\n"
            f"Subject of study: {self.thesis_topic}"
        )


def add_student():
    name = input("Input your name: ")
    while True :
        try :
            age = int(input("input your age : "))
            if age < 0 :
                print("age cannot be nagative 0 chose another number")
                continue
        except ValueError :
            print("====== age cannot be a letter pls input a number ======")
            continue
        break

    course = input("Input your course of study: ")
    email = input("Input your email: ")
    thesis_topic = input("Input your specialization: ")

  
    if thesis_topic.strip() == "":
        new_student = Student(name, age, course, email)
    else :
        new_student = GraduateStudent(
            name, age, course, email, thesis_topic
        )
    

    students.append(new_student)
    print("Student added successfully!")


add_student()

for s in students:
    print(s.introduce())

print("Total students:", len(students))
