# Geek is very fond of patterns. 
# Once, his teacher gave him a pattern to solve. 
# He gave Geek an integer n and asked him to build a pattern.
# Help Geek to build a star pattern.
# Output:
# 1 
# 0 1 
# 1 0 1
# 0 1 0 1 
# 1 0 1 0 1

class Solution:
    def printTriangle(self, N):
        for i in range(1, N + 1):
            for j in range(1, i + 1):
                print((i + j + 1) % 2, end=" ")
            print()
