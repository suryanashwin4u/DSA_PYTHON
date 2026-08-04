# Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
# Note: You need to solve this problem without utilizing the built-in sort function.

# expected optimal approach is the Dutch National Flag Algorithm.

# Complexities:
# Time: O(n)
# Space: O(1)

class Solution:
    def sort012(self, arr):
        
        low = 0
        mid = 0
        high = len(arr) - 1
        
        while mid <= high:
            
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
                
            elif arr[mid] == 1:
                mid += 1
                
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1