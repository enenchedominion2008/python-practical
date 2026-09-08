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

    if method == "add":

        first_number = int(input("input your first number >> "))

        second_number = int(input("input your second number >> "))

        result = add(first_number, second_number)
        
        print(f"result >> {result} ")

    elif method == "sub" :

        first_number = int(input("input your first number >> "))

        second_number = int(input("input your second number >> "))
        
        result = sub(first_number, second_number)
        
        print(f"result >> {result} ")

    elif method == "div" :

        first_number = int(input("input your first number >> "))

        second_number = int(input("input your second number >> "))

        result = div(first_number, second_number)

        print(f"result >> {result} ")

    elif method == "mul" :

        first_number = int(input("input your first number >> "))

        second_number = int(input("input your second number >> "))

        result = mul(first_number, second_number)

        print(f"result >> {result} ")
    elif method == "exit" :
        break
    else :
        print("🚫🚫  such is not part of the method of \n calculation list you can select by typing either \n (add) (sub) (div) (mul)  🚫🚫 \n ")
        

