# Given an array arr[]. 
# Rotate the array to the left (counter-clockwise direction) by d steps, 
# where d is a positive integer. 
# Do the mentioned change in the array in place.
# Note: Consider the array as circular.

class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)

        # If d is greater than array size
        d = d % n

        # Step 1: reverse first d elements
        self.reverse(arr, 0, d - 1)

        # Step 2: reverse remaining elements
        self.reverse(arr, d, n - 1)

        # Step 3: reverse whole array
        self.reverse(arr, 0, n - 1)

    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
