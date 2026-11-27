# Given a number n, return the count of digits in this number.
# Expected Complexities
# Time Complexity: O(log n)
# Auxiliary Space: O(1)


class Solution:
    def countDigits(self, n: int) -> int:
        if n == 0:
            return 1

        count = 0
        while n > 0:
            count += 1
            n //= 10
            
        return count