# EXE 1
# """names = ["Dominion", "John", "Mary"]
# my_iter = iter(names)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))"""

#EXE2

def count_to_five():
    yield 1
    yield 2 
    yield 3 
    yield 4
    yield 5
    for n in count_to_five():
        print(n)

