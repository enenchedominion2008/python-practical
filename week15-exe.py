import re

password = input('input your password:')
if len(password) != 8 :
    print("password must be up to 8 digit")
has_digit = bool(re.search(r"\d", password))
if has_digit == True :
    print("only numbers are allowed not letters")
else:
    text = password
    saved = re.sub(r"\d+","*",text)
    print(f"your password {saved} is been saved")

    