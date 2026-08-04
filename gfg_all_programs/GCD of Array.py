# Given an array of n positive integers, find the GCD of all the array elements.

from math import gcd
class Solution:
    def gcd(self, n, arr):
   
        result = arr[0]
        
        for i in range(1, n):
            result = gcd(result, arr[i])
            
            # Early stopping if GCD becomes 1
            if result == 1:
                return 1
        
        return result

