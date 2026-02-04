# Geek is very fond of patterns. 
# Once, his teacher gave him a pattern to solve. 
# He gave Geek an integer n and asked him to build a pattern.
# Help Geek build a star pattern.
# * * * * *
# * * * *
# * * *
# * *
# *

class Solution:
    def printTriangle(self, N):
        # Outer loop controls the number of rows
        # Starts from N and decreases to 1
        for i in range(N, 0, -1):
            
            # Inner loop prints stars in each row
            # Number of stars = current value of i
            for j in range(i):
                print("*", end=" ")
            
            # After printing stars of one row, move to next line
            print()


