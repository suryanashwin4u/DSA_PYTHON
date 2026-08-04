# Given a number n and a value k. 
# From the right, set the kth bit in the binary representation of n. 
# The position of the Least Significant Bit(or last bit) is 0, 
# the second last bit is 1 and so on. 

class Solution:
    def setKthBit(self, n, k):
        return n | (1 << k)