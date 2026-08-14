# Given an array arr[], generate and return all possible subarrays. 
# The subarrays must be returned in the following order:
#       1. Subarrays starting from the first element, followed by subarrays starting from the second element, and so on.
#       2. For each starting index, subarrays should be in increasing length.

# Time Complexity: O(n^3)
# Auxiliary Space: O(n^3)

class Solution:
    def getSubArrays(self, arr):
        res = []
        n = len(arr)
        
        # Outer loop for starting index
        for i in range(n):
            # Inner loop for ending index
            for j in range(i, n):
                # Slice the array from index i to j (inclusive)
                res.append(arr[i : j + 1])
                
        return res
    
    