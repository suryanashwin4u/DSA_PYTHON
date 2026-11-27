# Given an integer n, return all the divisors of n in the ascending order.

# Expected Complexities
# Time Complexity: O(sqrt(n))
# Auxiliary Space: O(sqrt(n))

class Solution:
    def getDivisors(self, n: int):
        small_divisors = []
        large_divisors = []
        
        i = 1
        while i * i <= n:
            if n % i == 0:
                small_divisors.append(i)
                if i != n // i:
                    large_divisors.append(n // i)
            i += 1
            
        # Combine smaller divisors and reversed larger divisors for sorted order
        return small_divisors + large_divisors[::-1]