# You are given an array arr[] consisting of positive integers. 
# Return the maximum of every adjacent pairs in the array.

class Solution:
    def maxAdj(self, arr):
        # This list will store the result
        result = []
        
        # Loop till second last element
        for i in range(len(arr) - 1):
            # Compare current element with next element
            # and append the maximum of the two
            result.append(max(arr[i], arr[i + 1]))
        
        # Return the list of strongest neighbours
        return result
