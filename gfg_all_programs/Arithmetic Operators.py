# Given two integer variables x and y. You need to perform the following operations:

# p = x + y, Addition
# q = x - y, Subtraction
# r = x * y, Multiplication
# s = x / y, Division
# t = x % y, Modulo


# Time Complexity: O(1)
# Auxiliary Space: O(1)

x = int(input())
y = int(input())

# code here
p = x + y
q = x - y
r = x * y
s = x // y
t = x % y

# The below code prints the output
print(p, q, r, s, t)