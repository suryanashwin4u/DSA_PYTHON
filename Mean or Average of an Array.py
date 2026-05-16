# Given an unsorted array arr[], the task is to find the mean of the array.

# Note: Return the floor value of the mean.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def findMean(self, arr):
        total = sum(arr)
        n = len(arr)
        return total // n   # floor division