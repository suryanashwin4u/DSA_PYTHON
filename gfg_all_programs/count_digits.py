# Given a positive integer n, 
# count the number of digits in n that divide n evenly 
# (i.e., without leaving a remainder). 
# Return the total number of such digits.

class Solution:
    def evenlyDivides(self, n):
        temp = n
        count = 0
        
        while n > 0:
            digit = n % 10
            if digit != 0 and temp % digit == 0:
                count += 1
            n //= 10
        
        return count

