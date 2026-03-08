# Check whether given two arrays a[] and b[] are identical or not. 
# Two arrays are called identical arrays if they contain the same element with the same count, 
# regardless of the order of elements.

class Solution:
    def isIdentical(self, a, b):
        return sorted(a) == sorted(b)