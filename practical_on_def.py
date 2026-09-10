def add(a, b) :
    return a + b
def sub(a, b) :
    return a - b
def div(a, b) :
    return a / b
def mul(a, b) :
    return a * b

method = ""

while method != "exit" :

    method = input("choses your method of calculation \n add \n sub \n div \n mul \n >>> : ")
    if method == "exit" :
        continue
    if method not in ["add","sub","div","mul"] :
        print(f"🚫🚫 such << {method} >> is not part of the option list you can select by typing either \n (add) (sub) (div) (mul)  🚫🚫 \n  ")
        continue
    while True :
        try:
            first_number = int(input("input your first number >> "))
            break
        except ValueError :
            print("\n 🚫🚫 that is not a valid  number \n you can only use numbers \n and not symbols or letters 🚫🚫 \n ")
    while True:
        try :
            second_number = int(input("input your second number >> "))
            break
        except ValueError :
            print("\n 🚫🚫 that is not a valid  number \n you can only use numbers \n and not symbols or letters 🚫🚫 \n ")
  

    if method == "add":

        result = add(first_number, second_number)
        
        print(f"result >> {result} ")

    elif method == "sub" :

        
        result = sub(first_number, second_number)
        
        print(f"result >> {result} ")

    elif method == "div" :
        while True :
            try :
                result = div(first_number, second_number)
                break
            except ZeroDivisionError :
                print(" 🚫🚫\n math error try a diffrent second number \n 🚫🚫 ")
                second_number = int(input("second number >> "))
            

        print(f"result >> {result} ")

    elif method == "mul" :

        result = mul(first_number, second_number)

        print(f"result >> {result} ")
    

