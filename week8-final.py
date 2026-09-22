option = ""
while True :
    print("welcome to the teachers dashboard kindly select an option ")
    print("(1) add student")
    print("(2) view student")
    print("(3) search")
    print("(4) exit")
    option = input("what do you want to do >> ")
    if option == "1" :
        while option != "done" :
            name = input("add student names type or type 'done' to exit >> ")
            if name == "done" :
                break
            with open("student.txt","a") as file :
                file.write(name+"\n")
    elif option == "2" :
        with open("student.txt","r") as file :
            for line in file :
                print(line,end="")
    elif option == "3" :
        search = input("search student >> ")
        with open("student.txt","r") as file :
           for line in file :
               if line.strip() == search:
                   print("student <<"+search+">>found") 
    elif option == "4" :
        break
    else :
        print("🚫🚫🚫 that is not a correct option \n please read well before \n preforming any action 🚫🚫🚫")

print("work saved✅")

            