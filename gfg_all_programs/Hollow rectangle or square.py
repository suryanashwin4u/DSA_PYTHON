# Given two integers n and m, print a hollow rectangle or square pattern consisting of n rows and m columns.

class Solution:
    def printHollowRect(self, n, m):
        for i in range(n):
            row = ""
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    row += "*"
                else:
                    row += " "
            print(row)