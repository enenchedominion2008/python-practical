import os 

# r = read 
# a = append 
# w = write 
# x = create


text = open("text.txt",'r')
#print(text.read())
#print(text.read(4))
print(text.readline())
print(text.readline())

# looping while reading a file contents it is just like using readline but printing everything not just one thing at a time 

for line in text :
    print(line)

# this is just basically closing the file it may not show much diffrence but closing it can do apply th changes that is being done to that file

text.close()

# moving on to append , Append creates the file if it dosnt exist

text = open("text.txt", "a")
text.write("Neil")
text.close()

text = open("text.txt")
print(text.read())
text.close

# overwriting a file 
text = open("over.txt","w")
text.write("i am overwriting everything in this file ")
text.close

text = open("over.txt")
print(text.read())
text.close

# two ways to create a new file 

# 1 this method creates a new file if it dosent
#  exist but it  is called 

text = open("form.txt","w")
text.close()

# 2 this method creates a new file but return an error if the 
#file exists also you would need to inport os 

if not os.path.exists("domi.txt") :
    text = open("domi.txt","x")
    text.close()

# deleat a file 
#avoid an error if it doesnt exit
if os.path.exists("domi.txt"):
    os.remove("domi.txt")
else :
    print("file does not exist")

# using the try and except to check if a file exist

try :
    text = open("class.txt")
    print(text.read())
except :
    print("the file you are searching for does not exist")

# 