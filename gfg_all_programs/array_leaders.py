# find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.
class Solution:
    def leaders(self, arr):
        n = len(arr)
        result = []

        # The rightmost element is always a leader
        max_right = arr[-1]
        result.append(max_right)

        # Traverse array from right to left
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_right:
                max_right = arr[i]
                result.append(arr[i])

        # Reverse to maintain original order
        result.reverse()
        return result
