# Given an array of positive integers. 
# Your task is to rearrange the array elements alternatively i.e. 
# first element should be the max value, 
# the second should be the min value, 
# the third should be the second max, 
# the fourth should be the second min, and so on.
# Note: Modify the original array itself. 
# Do it without using any extra space. 
# You do not have to return anything.


# Time Complexity: O(n log n)
# Auxiliary Space: O(1)

class Solution:

    def rearrange(self, arr):

        arr.sort()

        n = len(arr)

        max_idx = n - 1
        min_idx = 0

        max_elem = arr[-1] + 1

        for i in range(n):

            if i % 2 == 0:

                arr[i] += (arr[max_idx] % max_elem) * max_elem
                max_idx -= 1

            else:

                arr[i] += (arr[min_idx] % max_elem) * max_elem
                min_idx += 1

        for i in range(n):

            arr[i] //= max_elem