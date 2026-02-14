# Given an array, arr[] and an integer x, 
# return true if there exists a pair of elements in the array whose absolute difference is x, otherwise, return false.

from typing import List

class Solution:
    def findPair(self, arr: List[int], x: int) -> bool:
        n = len(arr)
        if n < 2:
            return False
        
        arr.sort()
        
        i = 0
        j = 1
        
        while i < n and j < n:
            if i != j and arr[j] - arr[i] == x:
                return True
            elif arr[j] - arr[i] < x:
                j += 1
            else:
                i += 1
            
            if i == j:
                j += 1
                
        return False