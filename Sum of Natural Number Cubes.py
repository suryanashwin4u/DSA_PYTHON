# Given an integer n, 
# calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.


class Solution:
    def sumOfSeries(self, n):
        # Sum of first n natural numbers
        s = n * (n + 1) // 2
        
        # Square of the sum
        return s * s
