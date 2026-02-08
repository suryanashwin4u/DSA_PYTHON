# Given an array arr of distinct integers. 
# Rearrange the array in such a way that the first element is the largest and the second element is the smallest, 
# the third element is the second largest and the fourth element is the second smallest, and so on.

class Solution:
    def alternateSort(self, arr):
        arr.sort()                 # Step 1: sort
        i, j = 0, len(arr) - 1
        result = []

        # Step 2: alternate max and min
        while i < j:
            result.append(arr[j])  # largest
            result.append(arr[i])  # smallest
            i += 1
            j -= 1

        # Step 3: if middle element exists
        if i == j:
            result.append(arr[i])

        return result