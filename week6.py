# looping in list in python could be done in diffrent ways 

'''squares = []
for i in range(1, 6):
    squares.append(i * i)
print(squares)   # [1, 4, 9, 16, 25]
'''
#  a shorter method for it

squares = [i * i for i in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

# the math behind the whole loop 

# The math, one pass at a time
# Pass 1 — i is 1
# Multiply 1 × 1 = 1. Put 1 in the list.
# List so far: [1]

# Pass 2 — i is 2
# Multiply 2 × 2 = 4. Put 4 in the list.
# List so far: [1, 4]

# Pass 3 — i is 3
# Multiply 3 × 3 = 9. Put 9 in the list.
# List so far: [1, 4, 9]

# Pass 4 — i is 4
# Multiply 4 × 4 = 16. Put 16 in the list.
# List so far: [1, 4, 9, 16]

# Pass 5 — i is 5
# Multiply 5 × 5 = 25. Put 25 in the list.
# List so far: [1, 4, 9, 16, 25]

# Then i has no more numbers to take, so the loop stops.

