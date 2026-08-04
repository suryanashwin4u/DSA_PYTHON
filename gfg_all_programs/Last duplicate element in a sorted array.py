# You are given a sorted array arr[] that may contain duplicate elements. 
# Your task is to find the index of the last occurrence of any duplicate element 
# and return the index along with the value of that element. 
# If no duplicate element is found, return [-1, -1].

class Solution:
    def dupLastIndex(self, arr):
        n = len(arr)
        
        # Traverse from end
        for i in range(n - 1, 0, -1):
            if arr[i] == arr[i - 1]:
                return [i, arr[i]]
        
        # No duplicate found
        return [-1, -1]
