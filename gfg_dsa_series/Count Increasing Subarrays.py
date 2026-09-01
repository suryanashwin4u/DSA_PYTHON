# Given an array arr[] of integers, 
# return the number of subarrays in arr[] which are strictly increasing with size greater or equal to 2. 
# A subarray is a contiguous part of array. 
# A subarray is strictly increasing if each element is greater then it's previous element if it exists.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def countIncreasing(self, arr):
        n = len(arr)
        if n < 2:
            return 0
    
        count = 0
        length = 1
    
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                length += 1
            else:
                count += (length * (length - 1)) // 2
                length = 1
    
        # Add the count for the last increasing contiguous segment
        count += (length * (length - 1)) // 2
    
        return count