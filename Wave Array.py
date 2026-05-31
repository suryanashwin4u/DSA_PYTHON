# Given an sorted array arr[] of integers. Sort the array into a wave-like array(In Place). In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5] ..... and so on. If there are multiple solutions, find the lexicographically smallest one.

# Note: The given array is sorted in ascending order, and modify the given array in-place without returning a new array.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def sortInWave(self, arr):
        n = len(arr)

        for i in range(0, n - 1, 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]