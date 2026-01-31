# Given an array arr. 
# Your task is to find the elements whose value is equal to that of its index value ( Consider 1-based indexing ).
# Note: There can be more than one element in the array which have the same value as its index. 
# You need to include every such element's index. Follows 1-based indexing of the array.

class Solution:
    def valueEqualToIndex(self, arr):
        result = []

        # Traverse array
        for i in range(len(arr)):
            # i is 0-based, index is i+1
            if arr[i] == i + 1:
                result.append(i + 1)

        return result