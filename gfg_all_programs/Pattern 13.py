# Geek is very fond of patterns. 
# Once, his teacher gave him a pattern to solve. 
# He gave Geek an integer n and asked him to build a pattern.
# Help Geek to build the pattern.

class Solution:
    def printTriangle(self, N):
        count = 1
        for i in range(1, N + 1):
            for j in range(i):
                print(count, end=" ")
                count += 1
            print()