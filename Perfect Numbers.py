# Given a number n, check if the number is perfect or not. 
# A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number.

class Solution:
    def isPerfect(self, n):
        if n <= 1:
            return False
        
        total = 1  # 1 is always a divisor
        
        i = 2
        while i * i <= n:
            if n % i == 0:
                total += i
                
                if i != n // i:   # avoid double count
                    total += n // i
            i += 1
        
        return total == n