# Geek is very fond of patterns. 
# Once, his teacher gave him a  pattern to solve.
# He gave Geek an integer n and asked him to build a pattern.
# Help Geek to build a pattern.
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3 
# 1 2  
# 1 

class Solution:
    def printTriangle(self, N):
        # Loop for rows (from N down to 1)
        for i in range(N, 0, -1):
            # Print numbers from 1 to i
            for j in range(1, i + 1):
                print(j, end=" ")
            # Move to next line after each row
            print()