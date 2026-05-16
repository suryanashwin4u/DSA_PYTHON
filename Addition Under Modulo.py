# Given three integers a, b, and M, compute the result of the modular addition operation:
# (a+b) mod M

# Note: Modular operations returns the remainder when divided by M. 
# The result will always lie in the range 0 and M - 1.

# Time Complexity: O(1)
# Auxiliary Space: O(1)

class Solution:
    def sumUnderModulo(self, a, b, M):
        return ((a % M) + (b % M)) % M