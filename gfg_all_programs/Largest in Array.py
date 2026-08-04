class Solution:
    def largest(self, arr):
        max_ele = arr[0]          # assume first element is largest
        for x in arr:             # single traversal
            if x > max_ele:
                max_ele = x
        return max_ele
