# Week 9: Exception Handling
#we have handled something like it already that is a try and exceept

"""try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except:
    print("That is not a valid number.")"""

# using the try and except function for multiple instances

"""try:
    number = int(input("Enter a number: "))

    result = 100 / number

    print(result)

except ValueError:
    print("You must enter a number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")"""

# using the finally block 
"""try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

finally:
    print("Program finished.")"""

# more example 
""""try:
    first = int(input("First number: "))
    second = int(input("Second number: "))

    result = first / second

    print("Result:", result)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print("Calculation completed.")

finally:
    print("Thank you for using the calculator."""""

# 