numbers = [1, 2, 3]
my_iterator = iter(numbers)

print(next(my_iterator))   # 1
print(next(my_iterator))   # 2
print(next(my_iterator))   # 3
print(next(my_iterator))   # crashes: StopIteration