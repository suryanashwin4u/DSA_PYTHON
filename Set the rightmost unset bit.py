# Given a non-negative number n . 
# The problem is to set the rightmost unset bit in the binary representation of n.

class Solution:
    def setBit(self, n):
        # Set the rightmost unset bit
        return n | (n + 1)
