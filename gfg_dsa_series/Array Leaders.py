# You are given an array arr of positive integers. 
# Your task is to find all the leaders in the array. 
# An element is considered a leader if it is greater than or equal to all elements to its right. 
# The rightmost element is always a leader.

# Time Complexity: O(n)
# Auxiliary Space: O(1)


class Solution:
    def leaders(self, arr):
        n = len(arr)
        result = []
        
        # Start with the rightmost element as the max
        max_from_right = arr[-1]
        result.append(max_from_right)
        
        # Traverse from right to left starting from second-to-last element
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_from_right:
                max_from_right = arr[i]
                result.append(max_from_right)
        
        # Reverse to restore the original order from left to right
        result.reverse()
        return result
