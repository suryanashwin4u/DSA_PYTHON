# Given a number n, check whether every bit in the binary representation of the given number is set or not.

# Return true if yes, otherwise false.

# Time Complexity: O(1)
# Auxiliary Space: O(1)

class Solution:
    def isBitSet(self, n):
        return n != 0 and (n & (n + 1)) == 0