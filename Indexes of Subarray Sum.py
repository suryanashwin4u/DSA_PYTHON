# Given an array arr[] containing only non-negative integers, 
# your task is to find a continuous subarray 
# (a contiguous sequence of elements) whose sum equals a specified value target. 
# You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. 
# You need to find the first subarray whose sum is equal to the target.

# Note: If no such array is possible then, return [-1].
# Time Complexity: O(n)
# Auxiliary Space: O(1)

#User function Template for python3

class Solution:
    def subarraySum(self, arr, target):
        
        left = 0
        curr_sum = 0
        
        for right in range(len(arr)):
            
            curr_sum += arr[right]
            
            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1
            
            if curr_sum == target:
                return [left + 1, right + 1]   # 1-based indexing
        
        return [-1]