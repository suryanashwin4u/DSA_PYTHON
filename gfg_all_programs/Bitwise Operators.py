# Given three positive integers a, b and c. Your task is to perform some bitwise operations on them as given below:
# 1. d = a ^ a
# 2. e = c ^ b
# 3. f = a & b
# 4. g = c | (a ^ a)
# 5. e = ~ e
# Note: ^ is for xor.
# Then print d e f g space seperately. Move the cursor to the next line after printing.

a = int(input())
b = int(input())
c = int(input())

# Do a ^ a
d = a ^ a

# Do c ^ b
e = c ^ b

# Do a & b
f = a & b

# Do c | (a ^ a)
g = c | (a ^ a)

# Do ~e
e = ~e

print(d, e, f, g)
