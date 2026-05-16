# Given an array arr[]. 
# Your task is to find the minimum and maximum elements in the array.
# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def getMinMax(self, arr):
        minimum = arr[0]
        maximum = arr[0]
        
        for x in arr:
            if x < minimum:
                minimum = x
            if x > maximum:
                maximum = x
        
        return [minimum, maximum]