# You are given two numbers n and p. You need to find n raise to the power p.
# RecursivePower(2, 3)
# = 2 * RecursivePower(2, 2)
# = 2 * (2 * RecursivePower(2, 1))
# = 2 * (2 * (2 * RecursivePower(2, 0)))
# = 2 * 2 * 2 * 1
# = 8

class Solution:
    def RecursivePower(self, n, p):
        # Base case
        if p == 0:
            return 1
        
        # Recursive case
        return n * self.RecursivePower(n, p - 1)