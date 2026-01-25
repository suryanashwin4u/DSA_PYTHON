# Given a number n, determine whether it is a prime number or not.
# Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

class Solution:
    def isPrime(self, n):
        # Step 1: Handle edge cases
        # Numbers less than or equal to 1 are NOT prime
        if n <= 1:
            return False
        
        # Step 2: 2 and 3 are prime numbers
        if n == 2 or n == 3:
            return True
        
        # Step 3: Eliminate even numbers and multiples of 3 early
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        # Step 4: Check divisibility from 5 to sqrt(n)
        # We increment by 6 because all primes > 3 are of the form 6k ± 1
        i = 5
        while i * i <= n:
            # Step 5: If divisible by i or i + 2, not prime
            if n % i == 0 or n % (i + 2) == 0:
                return False
            
            # Step 6: Move to next possible factor
            i += 6
        
        # Step 7: If no divisor found, it's prime
        return True