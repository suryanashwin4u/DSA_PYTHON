# Given a number n, print a diamond-shaped star pattern with 2n rows, 
# where the number of stars first increases and then decreases to form the diamond.

# Time Complexity: O(n^2)
# Auxiliary Space: O(1)

n = int(input())

# Upper half
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()

# Lower half
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()