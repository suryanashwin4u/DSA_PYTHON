# Given a positive integer n, 
# The task is to find the value of Σi F(i) 
# where i is from 1 to n and function F(i) is defined as the sum of all divisors of i.
# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def sumOfDivisors(self, n):
        ans = 0

        for i in range(1, n + 1):
            ans += i * (n // i)

        return ans