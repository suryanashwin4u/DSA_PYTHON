# You are given a number n. 
# You need to find the nth Fibonacci number.
# Note: F(n) = F(n-1) + F(n-2) ; where F(0) = 0 and F(1) = 1
# nthFibonacci(3)
# = nthFibonacci(2) + nthFibonacci(1)
# nthFibonacci(2)
# = nthFibonacci(1) + nthFibonacci(0)
# = 1 + 0 = 1
# nthFibonacci(1) = 1
# Final Answer = 1 + 1 = 2

class Solution:
    def nthFibonacci(self, n):
        # Base case: if n is 0 or 1, return n itself
        if n <= 1:
            return n

        # Recursive case
        return self.nthFibonacci(n - 1) + self.nthFibonacci(n - 2)