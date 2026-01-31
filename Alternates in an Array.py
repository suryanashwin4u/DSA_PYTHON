# You are given an array arr[], 
# the task is to return a list elements of arr in alternate order (starting from index 0)

class Solution:
    def getAlternates(self, arr):
        result = []
        
        # Traverse array by skipping one element each time
        for i in range(0, len(arr), 2):
            result.append(arr[i])
        
        return result
