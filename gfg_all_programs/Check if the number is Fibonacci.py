# Check if a given number N is the Fibonacci number. 
# A Fibonacci number is a number that occurs in the Fibonacci series.

class Solution:
    def checkFibonacci(self, N):
        a, b = 0, 1
        while b < N:
            a, b = b, a + b
        
        return "Yes" if N == b or N == 0 else "No"