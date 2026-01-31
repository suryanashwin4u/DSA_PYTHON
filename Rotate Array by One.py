# Given an array arr, rotate the array by one position in clockwise direction.

class Solution:
    def rotate(self, arr):
        """
        Rotates the array by one position in clockwise direction.
        The last element moves to the first position.
        """

        # Step 1: Store the last element of the array
        last_element = arr[-1]

        # Step 2: Shift all elements one position to the right
        # Start from the second last index and move backwards
        for i in range(len(arr) - 1, 0, -1):
            arr[i] = arr[i - 1]

        # Step 3: Place the last element at the first position
        arr[0] = last_element
