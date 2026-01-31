# Given a positive integer, n. Find the factorial of n.
# factorial(4)
# = 4 * factorial(3)
# = 4 * 3 * factorial(2)
# = 4 * 3 * 2 * factorial(1)
# = 4 * 3 * 2 * 1
# = 24

class Solution:
    def factorial(self, n: int) -> int:
        if n == 0:
            return 1
        return n * self.factorial(n - 1)