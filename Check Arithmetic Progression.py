# Given an array arr[] of integers. 
# Write a program to check whether an arithmetic progression 
# can be formed using all the given elements. 

class Solution:
    def checkIsAP(self, arr):
        n = len(arr)
        
        # Step 1: sort the array
        arr.sort()
        
        # Step 2: find common difference
        diff = arr[1] - arr[0]
        
        # Step 3: check all differences
        for i in range(1, n-1):
            if arr[i+1] - arr[i] != diff:
                return False
        
        return True