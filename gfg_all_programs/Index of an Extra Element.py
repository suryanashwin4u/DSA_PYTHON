# You have given two sorted arrays a[] & b[] of distinct elements. 
# The first array has one element extra added in between. 
# Return the index of the extra element.

# Note: 0-based indexing is followed.

class Solution:
    def findExtra(self, a, b):
        low, high = 0, len(b) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if a[mid] == b[mid]:
                low = mid + 1
            else:
                high = mid - 1
        
        return low