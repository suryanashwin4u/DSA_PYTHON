# Given a positive integer n, 
# find the number of perfect squares that are less than n in the sample space of perfect squares. 
# The sample space consists of all perfect squares starting from 1 (i.e., 1, 4, 9, 16, 25, …)

class Solution:
    def countSquares(self, n):
    # Count perfect squares strictly less than n
        return int((n - 1) ** 0.5)
