"""

Name = input("name : ")
birth_Year = input("birth year : ")
current_age = 2026-int(birth_Year)
next_year_age = current_age + 1 
print(f"welcome {Name} to our dashbored you are {current_age} years old \n and will be {next_year_age} next year \n which means you are elligeable to study at dominion tech institute")

"""
name = ""
while name != "exit":
    name = input("name (or 'exit' to quit): ")
    if name != "exit":

        birth_Year = input("birth year : ")
        age =  2026 - int(birth_Year) 
        days_old = age * 365
        if age % 2 == 0:
            parity = "even"
        else:
            parity = "odd"
    
        if age >= 16 :
            eligiblity = " eligible"
        else :
            eligiblity = "not  eligible"


        print(f"welcome {name.upper()} to our website you \n are {age} years old and {days_old} days old and is an {parity} number and \n it evalutes to be that you are \n {eligiblity.upper()} for the tech institute")
