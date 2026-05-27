# Given a number n, return the count of digits in this number.
# Time Complexity: O(log n)
# Auxiliary Space: O(log n)

class Solution:
    def countDigits(self, n):
        count = 0

        while n > 0:
            n = n // 10
            count += 1

        return count
