# Given two positive integers x and y, determine if y is a power of x. 
# If y is a power of x, return True. Otherwise, return False.

class Solution:
    def isPowerOfAnother(self, x, y):
        # Case 1: if x is 1
        if x == 1:
            return y == 1

        # Keep dividing y by x
        while y % x == 0:
            y = y // x

        # If y becomes 1, it is a power
        return y == 1
