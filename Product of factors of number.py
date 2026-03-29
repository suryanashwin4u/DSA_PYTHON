# Given a number N. Calculate the product of all factors of N. 
# Since Answer can be very large,compute the answer modulo 109+7.

class Solution:
    def factorProduct(self, N):
        MOD = 10**9 + 7
        product = 1
        
        i = 1
        while i * i <= N:
            if N % i == 0:
                if i == N // i:
                    product = (product * i) % MOD
                else:
                    product = (product * i * (N // i)) % MOD
            i += 1
        
        return product