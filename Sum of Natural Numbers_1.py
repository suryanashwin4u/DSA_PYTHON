# Given an integer n, your task is to compute the sum of all natural numbers from 1 to n (inclusive). 
# If n is 0, the sum should be 0.

# Time Complexity: O(1)
# Auxiliary Space: O(1)

class Solution:
    def sumOfNaturals(self, n):
        return n * (n + 1) // 2