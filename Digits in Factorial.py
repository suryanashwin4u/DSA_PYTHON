# Given an integer n, find the number of digits in the value of n factorial. 

# Time Complexity: O(1)
# Auxiliary Space: O(1)

# digits in n!
# =
# floor(log10(n!)) + 1

# digits in a number x
# =
# floor(log10(x)) + 1

import math

class Solution:
    def digitsInFactorial(self, n):
        if n <= 1:
            return 1

        x = n * math.log10(n / math.e)
        x += 0.5 * math.log10(2 * math.pi * n)

        return math.floor(x) + 1