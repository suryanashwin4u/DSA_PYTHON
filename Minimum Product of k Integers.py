# Given an array arr of positive integers, 
# return the minimum possible product of any k elements from the array. 
# Return the result modulo 1e9 + 7.

class Solution:
    def minProduct(self, arr, k):
        MOD = 10**9 + 7
        
        n = len(arr)
        k = min(k, n)   # handle edge case
        
        arr.sort()
        
        product = 1
        for i in range(k):
            product = (product * arr[i]) % MOD
        
        return product