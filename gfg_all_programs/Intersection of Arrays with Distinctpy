# Given two unsorted integer arrays a[] and b[] each consisting of distinct elements, 
# the task is to return the count of elements in the intersection (or common elements) of the two arrays.

# Intersection of two arrays can be defined as the set containing distinct common elements between the two arrays. 

class Solution:
    def intersectSize(self, a, b):
        # Store elements of array a in a set
        s = set(a)
        
        count = 0
        
        # Check elements of b in set
        for x in b:
            if x in s:
                count += 1
        
        return count