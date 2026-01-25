# Given an array, arr[] sorted in ascending order and an integer k. 
# Return true if k is present in the array, otherwise, false.

# User function Template for python3

class Solution:
    def searchInSorted(self, arr, k):
        # Initialize left and right pointers
        left = 0
        right = len(arr) - 1
        
        # Binary Search loop
        while left <= right:
            # Find the middle index
            mid = left + (right - left) // 2
            
            # If element found, return True
            if arr[mid] == k:
                return True
            
            # If middle element is smaller than k, search right half
            elif arr[mid] < k:
                left = mid + 1
            
            # If middle element is greater than k, search left half
            else:
                right = mid - 1
        
        # If element not found, return False
        return False