# You are given an integer array arr[]. 
# You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        max_so_far = arr[0]
        curr_max = arr[0]

        for i in range(1, len(arr)):
            curr_max = max(arr[i], curr_max + arr[i])
            max_so_far = max(max_so_far, curr_max)

        return max_so_far

