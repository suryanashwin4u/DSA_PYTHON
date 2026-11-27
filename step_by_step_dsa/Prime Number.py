# Given a number n, find if it is a prime number or not.

# Expected Complexities
# Time Complexity: O(sqrt(n))
# Auxiliary Space: O(1)

class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True