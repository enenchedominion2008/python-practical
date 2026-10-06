# def shout(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper

# @shout
# def greet():
#     return "hello"

# print(greet())   # HELLO

# decorators
def loud(func):
    def wrapper():
        result = func()
        print(result.upper())
    return wrapper

@loud
def greet():
    return "dominion"

greet()