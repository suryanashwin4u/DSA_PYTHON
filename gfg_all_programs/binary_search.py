class Solution:
    def binarysearch(self, arr, k):
        low = 0
        high = len(arr) - 1
        ans = -1   # to store result

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == k:
                ans = mid        # store index
                high = mid - 1   # move left for smallest index
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1

        return ans
