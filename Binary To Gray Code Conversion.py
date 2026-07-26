# Given a non-negative integer n, convert its binary representation into the corresponding Gray code and return the decimal value of the resulting Gray code.

# Time Complexity: O(log n)
# Auxiliary Space: O(1)

class Solution:
    def binaryToGray(self, n):
        if n == 0:
            return 0

        gray = 0
        msb = n.bit_length() - 1

        for i in range(msb, -1, -1):
            curr = (n >> i) & 1
            nxt = (n >> (i + 1)) & 1
            gray |= (curr ^ nxt) << i

        return gray
    
# or

class Solution:
    def binaryToGray(self, n):
        return n ^ (n >> 1)