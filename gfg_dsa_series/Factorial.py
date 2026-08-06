# Given a positive integer, n. Find the factorial of n.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def factorial(self, n: int) -> int: 
        # 0! and 1! are both 1
        ans = 1
        for i in range(2, n + 1):
            ans *= i
        return ans