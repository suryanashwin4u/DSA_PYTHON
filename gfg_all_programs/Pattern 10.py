# Geek is very fond of patterns. 
# Once, his teacher gave him a pattern to solve. 
# He gave Geek an integer n and asked him to build a pattern.
# Input: 5
# Output:
# * 
# * * 
# * * * 
# * * * * 
# * * * * *
# * * * *
# * * *
# * *
# *
# Help Geek to build a star pattern.

class Solution:
    def printTriangle(self, n):
        # Upper triangle
        for i in range(1, n + 1):
            print("* " * i)
        
        # Lower triangle
        for i in range(n - 1, 0, -1):
            print("* " * i)
