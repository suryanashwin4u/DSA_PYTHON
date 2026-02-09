# You are given a sorted array arr[] containing positive integers. 
# Your task is to remove all duplicate elements from this array such that each element appears only once. 
# Return an array containing these distinct elements in the same order as they appeared.

class Solution:
    def removeDuplicates(self, arr):
        if not arr:
            return []

        idx = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                arr[idx] = arr[i]
                idx += 1

        return arr[:idx]
