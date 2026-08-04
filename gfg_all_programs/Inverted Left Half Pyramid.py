# Given a number n. Print Inverted Left Half Pyramid with n lines.
# Note: There is a space between two adjacent stars (*) in the pattern.

class Solution:
    def printInvertedPyramid(self, n):
        for i in range(n, 0, -1):
            for j in range(i):
                print("*", end=" ")
            print()
