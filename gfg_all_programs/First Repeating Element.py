# Given an array arr[], find the first repeating element index. 
# The element should occur more than once and the index of its first occurrence should be the smallest.
# Note:- The position you return should be according to 1-based indexing. 

# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:
    def firstRepeated(self, arr):
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        for i in range(len(arr)):
            if freq[arr[i]] > 1:
                return i + 1

        return -1