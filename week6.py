# looping in list in python could be done in diffrent ways 

squares = []
for i in range(1, 6):
    squares.append(i * i)
print(squares)   # [1, 4, 9, 16, 25]

#  a shorter method for it

squares = [i * i for i in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]
