# Given an array arr[], find any subsequence of three elements such that, arr[i] < arr[j] < arr[k] and (i < j < k).

# If such a subsequence exists, return the three elements as an array. Otherwise, return an empty array.

# Note:

# The driver code will print 1 if the returned subsequence is valid and present in the array.
# The driver code will print 0 if no such subsequence exists.
# If the returned subsequence does not satisfy the required format or conditions, the output will be -1.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def find3Numbers(self, arr):
        n = len(arr)
        if n < 3:
            return []
    
        # left_min[i] stores the index of the minimum element to the left of i
        left_min = [-1] * n
        min_idx = 0
        for i in range(1, n):
            if arr[i] <= arr[min_idx]:
                min_idx = i
            else:
                left_min[i] = min_idx
    
        # right_max[i] stores the index of the maximum element to the right of i
        right_max = [-1] * n
        max_idx = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[max_idx]:
                max_idx = i
            else:
                right_max[i] = max_idx
    
        # Find an index i where both left smaller and right greater elements exist
        for i in range(n):
            if left_min[i] != -1 and right_max[i] != -1:
                return [arr[left_min[i]], arr[i], arr[right_max[i]]]
    
        return []