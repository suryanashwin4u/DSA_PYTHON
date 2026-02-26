# Given a number as string(n) , 
# find the remainder of the number when it is divided by 7

class Solution:
    def remainderWith7(self, n):
        remainder = 0
        for digit in n:
            remainder = (remainder * 10 + int(digit)) % 7
        return remainder