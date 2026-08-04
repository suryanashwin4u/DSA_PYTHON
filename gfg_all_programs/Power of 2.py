# Given a non-negative integer n. 
# You have to check if it is a power of 2 or not.

class Solution:
    def isPowerofTwo(self, n):
        # A number must be positive to be a power of 2
        if n <= 0:
            return False
        
        # For powers of 2, only one bit is set in binary.
        # n & (n - 1) removes the rightmost set bit.
        # If the result is 0, then n had only one set bit.
        return (n & (n - 1)) == 0