# Given two integers n and m, print a solid rectangle pattern consisting of n rows and m columns.

# Note: There is a space between two adjacent stars (*) in the pattern.

class Solution:
    def printSolidRect(self, n, m):
        for i in range(n):
            for j in range(m):
                print("*", end=" ")
            print()