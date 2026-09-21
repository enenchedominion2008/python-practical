with open("form.txt", "r") as text :
    line = text.readline()
print(line)

# reading multiple lines 
with open("form.txt","r" ) as text :
    print(text.readline())
    print(text.readline())

# reading all lines 
with open("text.txt","r") as file :
    names = file.readlines()
    print(names)

# creatung if files using the x and the while

with open("domi.txt","x") as file :
    file.write("hello")

# appending using the with 
# with open("over.txt","a") as text :
#     text.write("\ndominion")

