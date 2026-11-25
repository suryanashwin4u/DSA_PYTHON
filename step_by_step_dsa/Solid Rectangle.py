# Given two integers n and m, print a solid rectangle pattern of n rows and m columns using the "*" character.

# Expected Complexities
# Time Complexity: O(n * m)
# Auxiliary Space: O(1)

class Solution:
    def printSolidRectangle(self, n, m):
        # code here
        for i in range(n):
            for j in range(m):
                print('* ',end='')
            print()