# Given a number n, return the count of digits in this number.
# Time Complexity: O(log n)
# Auxiliary Space: O(log n)

class Solution:
    def countDigits(self, n: int) -> int:
        count = 0
        while n > 0:
            count += 1
            n //= 10
        return count