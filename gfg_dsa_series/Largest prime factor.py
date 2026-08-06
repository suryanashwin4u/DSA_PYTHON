# Given a number n, your task is to find the largest prime factor of n.

# Time Complexity: O(sqrt(n))
# Auxiliary Space: O(1)

class Solution:
    def largestPrimeFactor (self, n: int) -> int:
        max_prime = -1
        
        # Check divisibility by 2
        while n % 2 == 0:
            max_prime = 2
            n //= 2
            
        # Check odd factors from 3 up to sqrt(n)
        i = 3
        while i * i <= n:
            while n % i == 0:
                max_prime = i
                n //= i
            i += 2
            
        # If n is still greater than 2, then n itself is a prime factor
        if n > 2:
            max_prime = n
            
        return max_prime