# Given an array arr, you need to reverse a subarray of that array. 
# The range of this subarray is given by indices l and r (1-based indexing).

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def reverseSubArray(self, arr, l, r):
        l -= 1
        r -= 1

        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        return arr