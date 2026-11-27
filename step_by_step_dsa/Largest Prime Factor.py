# Given a number n, your task is to find the largest prime factor of n.

# Expected Complexities
# Time Complexity: O(sqrt(n))
# Auxiliary Space: O(1)

class Solution:
    def largestPrimeFactor(self, n: int) -> int:
        max_prime = -1

        # Remove all factors of 2
        while n % 2 == 0:
            max_prime = 2
            n //= 2

        # Check odd factors up to sqrt(n)
        i = 3
        while i * i <= n:
            while n % i == 0:
                max_prime = i
                n //= i
            i += 2

        # If remaining n is a prime greater than 2, it is the largest prime factor
        if n > 2:
            max_prime = n

        return max_prime