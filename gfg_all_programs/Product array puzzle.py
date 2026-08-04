# Given an array, arr[] construct a product array, 
# res[] where each element in res[i] is the product of all elements in arr[] except arr[i]. 
# Return this resultant array, res[].
# Note: Each element is res[] lies inside the 32-bit integer range.

class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)
        res = [1] * n
        
        # Step 1: Calculate Prefix Products
        # Store the product of all elements to the left of i in res[i]
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= arr[i]
            
        # Step 2: Calculate Suffix Products on the fly
        # Multiply the existing prefix product by the product of all elements to the right
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= arr[i]
            
        return res