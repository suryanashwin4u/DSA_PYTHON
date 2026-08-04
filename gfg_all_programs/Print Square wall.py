# Given an integer n,  write a program to print the square wall of size n using a single loop and string multiplication. 

# Time Complexity: O(n)
# Auxiliary Space: O(1)

n = int(input())

for _ in range(n):
    print("* " * n)