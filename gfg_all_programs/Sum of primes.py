# You are given an integer n. 
# Your task is to calculate the sum of primes present as digits of a given number n.

class Solution:
    def primeSum(self, n):
        prime_digits = {2, 3, 5, 7}
        total = 0
        
        while n > 0:
            digit = n % 10
            if digit in prime_digits:
                total += digit
            n //= 10
            
        return total