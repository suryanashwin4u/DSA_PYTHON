# A Krishnamurthy number is a number whose sum of the factorial of digits is equal to the number itself. 
# Given a number N as input. 
# Print "YES" if it's a Krishnamurthy Number, else Print "NO".

class Solution:
    def isKrishnamurthy(self, N):
        fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        
        original = N
        sum_fact = 0
        
        while N > 0:
            digit = N % 10
            sum_fact += fact[digit]
            N //= 10
        
        return "YES" if sum_fact == original else "NO"