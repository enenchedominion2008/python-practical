class Student :


    def __init__(self,name,age):
        self.name = name
        self.age = age 

    def introduce(self):
        print("my name is" , self.name)
        print("i am" ,self.age)

student1 = Student("Dominion",20)
student2 = Student("John",21)
student3 = Student("Divine",20)

student1.introduce()
student2.introduce()
student3.introduce()