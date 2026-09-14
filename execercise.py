#excercise 1 
# working on reversing strings 
# words = "i love python"
# words = words.split() 
# reverse = words[::-1]
# reverse = " ".join(reverse)
# print(reverse)

# excercise 2
#counting the leanght of a raw sentence 
# word = "hello how are you"
# word = word.split()
# print(len(word))

# execercise 3 
# creating a password of 8 digit
"""username = ""
while username != "exit" :
    username = input("please put your user name : ")
    while True :
           try :
                  password = input("input your password : ")
                  break
           except ValueError :
                  print("use numbers only")
    
    if password != "12345678" :
            print("please cheack your password and try again")
    else :
            print(f"welcome to your account dear {username.upper()}")
"""
password = input("input your password : ")

# Check 1: length
long_enough = len(password) >= 8

# Check 2: contains at least one digit
has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True

# Final decision: BOTH conditions must be true
if long_enough and has_digit:
    print("valid password")
else:
    print("invalid password")
    