# Given a number N, check if N is power of 4 or not.

class Solution():
    def isPowerofFour(self, n):
        if n <= 0:
            return 0
        
        while n % 4 == 0:
            n = n // 4
        
        if n == 1:
            return 1
        else:
            return 0
