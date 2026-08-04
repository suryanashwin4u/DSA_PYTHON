# Given two sorted arrays arr1 and arr2 of distinct elements. 
# Given a value x. 
# The problem is to count all pairs from both arrays whose sum equals x.
# Note: The pair has an element from each array.

class Solution:
    def countPairs(self, arr1, arr2, x):
        i = 0
        j = len(arr2) - 1
        count = 0
        
        while i < len(arr1) and j >= 0:
            s = arr1[i] + arr2[j]
            
            if s == x:
                count += 1
                i += 1
                j -= 1
            elif s < x:
                i += 1
            else:
                j -= 1
        
        return count