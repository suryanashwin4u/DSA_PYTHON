# Given an array arr of even size, 
# the task is to find a minimum value that can be added to an element so that the array becomes balanced. 
# An array is balanced if the sum of the left half of the array elements is equal to the sum of the right half.

class Solution:
    def min_value_to_balance(self, arr):
        n = len(arr)
        mid = n // 2

        # Sum of left half
        left_sum = sum(arr[:mid])

        # Sum of right half
        right_sum = sum(arr[mid:])

        # Minimum value needed
        return abs(left_sum - right_sum)
