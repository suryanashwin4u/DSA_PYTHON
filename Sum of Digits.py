# You are given a number n. 
# You need to find the sum of digits of n.

class Solution:
    def sumOfDigits(self, n):
        total = 0
        
        while n > 0:
            digit = n % 10      # get last digit
            total += digit      # add digit to sum
            n = n // 10         # remove last digit
        
        return total
