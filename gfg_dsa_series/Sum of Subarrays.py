# Given an array arr[], find the sum of all the subarrays of the given array.

# Note: It is guaranteed that the total sum will fit within a 32-bit integer range.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def subarraySum(self, arr):
        n = len(arr)
        total_sum = 0
        
        for i in range(n):
            # Calculate total contribution of arr[i]
            count = (i + 1) * (n - i)
            total_sum += arr[i] * count
            
        return total_sum