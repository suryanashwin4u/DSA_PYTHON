# Given a single integer N, 
# your task is to find the sum of the square of the first N odd natural Numbers.

class Solution:
    def sum_of_square_oddNumbers(self, n):
        # Formula: N(2N-1)(2N+1)/3
        return (n * (2*n - 1) * (2*n + 1)) // 3