# Given a number n, 
# return an array containing the first n Fibonacci numbers.
# Note: The first two numbers of the series are 0 and 1.


class Solution:
    # Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self, n):
        
        # If n is 1, return only the first Fibonacci number
        if n == 1:
            return [0]
        
        # Initialize the list with first two Fibonacci numbers
        fib = [0, 1]
        
        # Generate remaining Fibonacci numbers
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        
        return fib
