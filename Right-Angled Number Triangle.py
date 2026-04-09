# Given a number n. The task is to print Right-Angled Number Triangle with n lines.

# Note: There is a space between two adjacent number in the pattern.

class Solution:
    def printRightTriangle(self, n):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()