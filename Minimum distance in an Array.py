# You are given an array, arr[]. 
# Find the minimum index based distance between two distinct elements of the array, x and y. 
# Return -1, if either x or y does not exist in the array.

class Solution:
    def minDist(self, arr, x, y):
        last_x = -1
        last_y = -1
        min_dist = float('inf')

        for i in range(len(arr)):
            if arr[i] == x:
                last_x = i

            if arr[i] == y:
                last_y = i

            if last_x != -1 and last_y != -1:
                min_dist = min(min_dist, abs(last_x - last_y))

        return -1 if min_dist == float('inf') else min_dist