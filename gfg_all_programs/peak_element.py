# You are given an array arr[] where no two adjacent elements are same, 
# find the index of a peak element. An element is considered to be a peak if it is greater than its adjacent elements (if they exist).
# If there are multiple peak elements, 
# Return index of any one of them. The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".

class Solution:
    def peakElement(self, arr):
        n = len(arr)
        l, h = 0, n - 1   # low and high pointers for binary search

        while l < h:
            mid = (l + h) // 2   # find middle index

            # If mid element is smaller than next,
            # then a peak must exist on the right side
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                # Otherwise, a peak lies on the left side or at mid
                h = mid

        # When l == h, it points to a peak element index
        return l