# Geek is very fond of patterns. 
# Once, his teacher gave him a pattern to solve. 
# He gave Ram an integer n and asked him to build a pattern.
# Help Ram build a pattern.

class Solution:
    def printTriangle(self, n):
        for i in range(1, n + 1):
            # print leading spaces
            print(" " * (n - i), end="")
            
            # print stars
            print("*" * (2 * i - 1))
