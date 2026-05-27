# You are given an array of integers. 
# Return the sum of all the array elements.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def arraySum(self, arr):
        sum = 0
        
        for i in arr:
            sum += i
            
        return sum