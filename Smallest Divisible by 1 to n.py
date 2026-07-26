# Given a number n, find an integer denoting the smallest number evenly divisible by each number from 1 to n.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

from math import gcd

class Solution:
    def getSmallestDivNum(self, n):
        lcm = 1
        for i in range(2, n + 1):
            lcm = lcm * i // gcd(lcm, i)
        return lcm