# Given an array arr[], check whether it is sorted in non-decreasing order. 
# Return true if it is sorted otherwise false.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def isSorted(self, arr):
        # Iterate through the array and check if any element 
        # is greater than the next element
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True