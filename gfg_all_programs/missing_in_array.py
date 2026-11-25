# Given an array arr[] of size n - 1 containing distinct integers in the range [1, n]. 
# The array represents a permutation of the integers from 1 to n with exactly one element missing.

# Find and return the missing element.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def missingNum(self, arr: list[int]) -> int:
        n = len(arr) + 1
        total_sum = n * (n + 1) // 2
        actual_sum = sum(arr)
        return total_sum - actual_sum

