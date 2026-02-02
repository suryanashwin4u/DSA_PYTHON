# Given a number n. 
# You have to check whether it is sparse or not.
# Note: A number is said to be a sparse number 
# if no two or more consecutive bits are set in the binary representation.

class Solution:
    def isSparse(self, n):
        # If n has consecutive set bits, 
        # n & (n >> 1) will be non-zero
        if (n & (n >> 1)) == 0:
            return True
        else:
            return False
