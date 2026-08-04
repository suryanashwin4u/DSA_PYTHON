# Given a number n, print pyramid pattern with n lines.

class Solution:
    def printPyramid(self, n):
        for i in range(1, n + 1):
            # print spaces
            print(" " * (n - i), end="")
            
            # print stars
            print("*" * (2 * i - 1))