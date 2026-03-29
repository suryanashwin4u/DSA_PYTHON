# Given the maximum possible area of the right angle triangle for a fixed length of hypotenuse. 
# The task is to find the length of hypotenuse.

# Note: If the answer comes in Decimal, find it's Floor value.

import math

class Solution:
    def getHypotenuse(self, N):
        return int(2 * math.sqrt(N))