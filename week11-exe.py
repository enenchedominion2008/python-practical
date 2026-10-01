# class Student:

#     def __init__(self,name,age,course):
#         self.name = name
#         self.age = age
#         self.course = course
    
#     def introduce(self) :
#         print("my name is" , self.name)
#         print("my age is", self.age)
#         print("i am studying",self.course)
#     def study(self):
#         print(self.name,"is studying",self.course)
#     def birthday(self) :
#         self.age = self.age + 1
#         print(self.name,"is +1 today he is",self.age,"years old today")

    
# student1 = Student("Dominion",30 ,"computer science,software engineering")
# student2 = Student("Divine", 50,"computer science")
 
# student2.introduce()
# student1.study()
# student1.birthday() 
# student1.introduce()    


# inheritance exercise

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        return f"my name is {self.name}, studying {self.course}"


class GraduateStudent(Student):
    def __init__(self, name, age, course, thesis_topic):
        super().__init__(name, age, course)
        self.thesis_topic = thesis_topic
    def introduce(self):
        return f"my  name is {self.name} and am studying {self.course} and {self.thesis_topic}"


grad = GraduateStudent("Dominion", 21, "Computer Science", "AI Ethics")
print(grad.introduce())     
print(grad.thesis_topic)