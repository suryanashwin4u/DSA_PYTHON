# Given an array arr[] of positive integers.The task is to complete the insertsort() function which is used to implement Insertion Sort.

# Time Complexity: O(n^2)
# Auxiliary Space: O(1)

class Solution:
    def insertionSort(self, arr):
        n = len(arr)

        for i in range(1, n):
            key = arr[i]
            j = i - 1

            # Shift elements greater than key
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

            # Place key at correct position
            arr[j + 1] = key