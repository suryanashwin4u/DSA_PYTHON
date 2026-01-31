# Given an array arr[]. 
# Your task is to find the minimum and maximum elements in the array.

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