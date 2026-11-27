# For an integer n, find the number of trailing zeroes in n!.

# Expected Complexities
# Time Complexity: O(log n)
# Auxiliary Space: O(1)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            count += n // 5
            n //= 5
        return count