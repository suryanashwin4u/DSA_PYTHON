# Given two integers n and m (m != 0). 
# The problem is to find the number closest to n and divisible by m. 
# If there is more than one such number, then output the one having the maximum absolute value.

# Expected Complexities
# Time Complexity: O(1)
# Auxiliary Space: O(1)

class Solution:
    def closestNumber(self, n, m):
        q = int(n / m)          # truncates toward zero (unlike // in Python)
        n1 = m * q
        n2 = m * (q + 1) if (n * m) > 0 else m * (q - 1)

        d1 = abs(n - n1)
        d2 = abs(n - n2)

        if d1 < d2:
            return n1
        if d2 < d1:
            return n2
        
        return n1 if abs(n1) >= abs(n2) else n2