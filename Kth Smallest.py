# Given an integer array arr[] and an integer k, 
# find and return the kth smallest element in the given array.
# Note: The kth smallest element is determined based on the sorted order of the array.

# Time Complexity: O(n log k)
# Auxiliary Space: O(k)

import heapq

class Solution:
    def kthSmallest(self, arr, k):

        max_heap = []

        for num in arr:

            # Python has min heap only
            # so store negative values
            heapq.heappush(max_heap, -num)

            # keep only k elements
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return -max_heap[0]