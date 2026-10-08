import re 
password = input("input your password: ")
if len(password) < 8 :
    print("password is lesser than 8 password must be higher than 8")
else : 
    print("password done")
    has_digit = bool(re.search(r"\d",password))
    if has_digit:
        print("password is valid")
    else :
        print("password must contain a digit")





# doing it with functions 
"""
import re 

def validate_password(password):
    if len(password) < 8:
        print("Password is too short. It must be 8 or more characters.")
        return False
    
    print("Length checked successfully.")
    
    # Check if the password contains a digit
    has_digit = bool(re.search(r"\d", password))
    
    if has_digit:
        print("Password is valid!")
        return True
    else:
        print("Password invalid: Must contain at least one digit.")
        return False

# --- How to use the function ---
user_password = input("Input your password: ")
is_valid = validate_password(user_password)"""
