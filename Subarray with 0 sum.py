# Given an array of integers, arr[]. 
# Find if there is a subarray (of size at least one) with 0 sum. 
# Return true/false depending upon whether there is a subarray present with 0-sum or not. 

# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:
    
    # Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self, arr):
        
        s = set()
        prefix = 0
        
        for num in arr:
            prefix += num
            
            if prefix == 0 or num == 0 or prefix in s:
                return True
            
            s.add(prefix)
        
        return False