# Given an array arr[]. The task is to find the largest element and return it.
from typing import List

class Solution:
    def largest(self, arr: List[int]) -> int:
        max_val = arr[0]   # initialize with first element
        
        for i in range(1, len(arr)):
            if arr[i] > max_val:
                max_val = arr[i]
                
        return max_val