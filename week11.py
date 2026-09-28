# class Student :


#     def __init__(self,name,age):
#         self.name = name
#         self.age = age 

#     def introduce(self):
#         print("my name is" , self.name)
#         print("i am" ,self.age)

# student1 = Student("Dominion",20)
# student2 = Student("John",21)
# student3 = Student("Divine",20)

# student1.introduce()
# student2.introduce()
# student3.introduce()
# student1.age = 23
# student1.introduce()

class Student:

    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course
    
    def introduce(self) :
        print("my name is" , self.name)
        print("my age is", self.age)
        print("i am studying",self.course)
    def study(self):
        print(self.name,"is studying",self.course)
    def birthday(self) :
        self.age = self.age + 1
        print(self.name,"is +1 today he is",self.age,"years old today")
    
student1 = Student("Dominion",30 ,"computer science")
student2 = Student("Divine", 50,"computer science")
 
student1.introduce()
student2.introduce()
student1.study()
student1.birthday()

"""
class Book :
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def summery(self):
        return f"{self.title} by {self.author}"
    
    
story1 = Book("Animal Farm ","George Orwell")
story2 = Book("the bad boy","john")
print(story1.summery())
print(story2.summery())
"""
