# Given an integer n, print a solid square pattern of size n × n using "* " (a star followed by exactly one space).
# Time Complexity: O(n)
# Auxiliary Space: O(1)


n = int(input())

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

