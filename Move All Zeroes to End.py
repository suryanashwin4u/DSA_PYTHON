# You are given an array arr[] of non-negative integers. 
# You have to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. 
# The operation must be performed in place, meaning you should not use extra space for another array.

class Solution:
    def pushZerosToEnd(self, arr):
        pos = 0  # position for next non-zero

        for i in range(len(arr)):
            if arr[i] != 0:
                arr[pos], arr[i] = arr[i], arr[pos]
                pos += 1