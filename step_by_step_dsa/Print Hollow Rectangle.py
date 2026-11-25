# Given two integers n and m, print a hollow rectangle pattern consisting of n rows and m columns using '*' character. 

# Expected Complexities
# Time Complexity: O(n * m)
# Auxiliary Space: O(1)

class Solution:
    def printHollowRect(self, n, m):
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i == 1 or i == n or j == 1 or j == m:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()