option = ""
while True :
    print("welcome to the teachers dashboard kindly select an option ")
    print("(1) add student")
    print("(2) view student")
    print("(3) search")
    print("(4) exit")

    option = input("what do you want to do >> ")

    if option == "1" :

        while True :

            name = input("add student names type or type 'done' to exit >> ")
            if name.strip() == "" :
                print("🚫🚫🚫  error name cannot be empty 🚫🚫🚫 ")
                continue
      

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

        found = False

        with open("student.txt","r") as file :
           
           for line in file :
               
               if line.strip().lower() == search.lower():
                   
                   found = True 
                   break 
        if found :
            print("student <<"+search+">> found")
        else :
            print("student <<"+search+">> not found")
    elif option == "4" :
        break
    else :
        print(f"🚫🚫🚫  please \n<<<({option})>>\n is not a correct option \n please read well before \n preforming any action 🚫🚫🚫")

print("work saved✅")

            
