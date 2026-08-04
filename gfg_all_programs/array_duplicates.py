# Use each value as an index and mark it negative; if already negative, it is a duplicate.
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