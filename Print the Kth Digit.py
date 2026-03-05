# Given two numbers a and b, find kth digit from right of ab.
class Solution:
    def kthDigit(self, a, b, k):
        num = a ** b          # calculate a^b
        num = num // (10 ** (k - 1))  # remove last k-1 digits
        return num % 10       # return kth digit from right
