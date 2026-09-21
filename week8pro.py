# try :
#     with open("week.txt","x") as file :
#         file.write("hello")
# except :
#     print("file already exists")

# with open("week.txt","w") as file :
#     file.write("i am rewrithing everything in this file")

# with open("week.txt","a") as file :
#     file.write("\n also adding this")

# with open("week.txt", "r") as file:
#     for line in file:
#         print(line)

# week 8 practical
name = ""
while name != "exit" :
    name = input("input your name >> ")
    with open("week.txt","a") as file :
        file.write(name+"\n")
if name == "exit" :
    with open("week.txt","r") as file :
        for line in file :
            print(line)