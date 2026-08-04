# Given an array, arr[] of n integers, and an integer element x, 
# find whether element x is present in the array. 
# Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.
# Time Complexity: O(n)
# Auxiliary Space: O(1)


class Solution:
    def search(self, arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1
