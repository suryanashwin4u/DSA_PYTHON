# You are given a positive integer n, 
# you need to add all the digits of n and create a new number. 
# Perform this operation until the resultant number has only one digit in it. 
# Return the final number obtained after performing the given operation.

class Solution:
    def singleDigit(self, n):
        if n == 0:
            return 0
        if n % 9 == 0:
            return 9
        return n % 9


class Solution:
    def singleDigit(self, n):
        return 1 + (n - 1) % 9