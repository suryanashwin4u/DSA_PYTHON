# Given an integer array arr[] and an integer k, reverse every consecutive group of k elements. 
# If fewer than k elements remain at the end, reverse all of them.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def reverseInGroups(self, arr, k):
        n = len(arr)
        
        # Process the array in steps of size k
        for i in range(0, n, k):
            # Define two pointers for the current group
            left = i
            # Make sure right pointer doesn't exceed array bounds
            right = min(i + k - 1, n - 1)
            
            # Reverse elements in the current sub-array in-place
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        
        return arr