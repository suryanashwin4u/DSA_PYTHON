# Given a number N. Check whether it is divisible by the sum of its digits or not.

class Solution:
    def isDivisible(self, N):
        temp = N
        digit_sum = 0
        
        while N > 0:
            digit_sum += N % 10
            N //= 10
        
        if temp % digit_sum == 0:
            return 1
        else:
            return 0