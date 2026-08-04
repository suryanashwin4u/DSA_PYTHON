# Given an array arr[]. 
# find the minimum difference between any pair in the given array.

class Solution:
    def minimumDifference(self, arr):
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Initialize minimum difference
        min_diff = float('inf')
        
        # Step 3: Compare adjacent elements
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
        
        return min_diff