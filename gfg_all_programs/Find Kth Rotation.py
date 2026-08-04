# Given an increasing sorted rotated array arr[] of distinct integers. 
# The array is right-rotated k times. Find the value of k.
# Let's suppose we have an array arr[] = [2, 4, 6, 9], 
# if we rotate it by 2 times it will look like this:
# After 1st Rotation : [9, 2, 4, 6]
# After 2nd Rotation : [6, 9, 2, 4]

class Solution:
    def findKRotation(self, arr):
        n = len(arr)
        
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                return i
        
        return 0