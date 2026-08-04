# Given an array arr[] consisting of only 0's and 1's. 
# Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.
# Complexity
# Time: O(n)
# Space: O(1)

class Solution:
    def segregate0and1(self, arr):
        left = 0
        right = len(arr) - 1

        while left < right:

            while left < right and arr[left] == 0:
                left += 1

            while left < right and arr[right] == 1:
                right -= 1

            if left < right:
                arr[left], arr[right] = arr[right], arr[left]