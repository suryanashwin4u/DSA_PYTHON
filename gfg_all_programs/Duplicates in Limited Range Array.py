# Given an array arr[] of size n, containing elements from the range 1 to n, 
# and each element appears at most twice, return an array of all the integers that appears twice.

# Note: You can return the elements in any order but the driver code will print them in sorted order.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def findDuplicates(self, arr):
        res = []

        for i in range(len(arr)):
            idx = abs(arr[i]) - 1   # value → index

            if arr[idx] < 0:        # already visited
                res.append(abs(arr[i]))
            else:
                arr[idx] = -arr[idx]  # mark as visited

        return res
