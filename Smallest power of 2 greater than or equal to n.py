# Given a number N.
# Find the nearest number which is a power of 2 and greater than or equal to N.

class Solution:
    def nearestPowerOf2(self, N):
        if (N & (N - 1)) == 0:
            return N
        return 1 << N.bit_length()
