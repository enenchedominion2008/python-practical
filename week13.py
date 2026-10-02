# iter() and next() — what for is secretly doing

#Every time you've written a for loop, Python has secretly been doing this:


"""numbers = [1, 2, 3]
my_iterator = iter(numbers)

print(next(my_iterator))   # 1
print(next(my_iterator))   # 2
print(next(my_iterator))   # 3
print(next(my_iterator))   # crashes: StopIteration"""

# Generators — functions that pause and resume

# A generator is a special kind of function that doesn't run start-to-finish in one go — it can pause, hand back a value, and later resume exactly where it left off. The keyword that makes this happen is yield, used instead of return


def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
counter = count_up_to(3)
print(next(counter))   # 1
print(next(counter))   # 2
print(next(counter))   # 3