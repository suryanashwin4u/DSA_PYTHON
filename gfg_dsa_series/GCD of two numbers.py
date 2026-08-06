# Given two positive integers a and b, find GCD of a and b.

# Note: Don't use the inbuilt gcd function

# Time Complexity: O(log(min(a, b)))
# Auxiliary Space: O(1)

class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a