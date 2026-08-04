# You are given an array of integers, 
# your task is to divide the array into two sub-arrays (left and right) containing half of the array elements. 
# Find the sum of the subarrays and then return the multiply of both the subarrays.

# Note: If the length of the array is odd then the right half will contain one element more than the left half.

class Solution:
    def multiply(self, arr):
        n = len(arr)
        mid = n // 2
        
        left_sum = 0
        right_sum = 0
        
        # Sum of left half
        for i in range(mid):
            left_sum += arr[i]
        
        # Sum of right half
        for i in range(mid, n):
            right_sum += arr[i]
        
        return left_sum * right_sum
