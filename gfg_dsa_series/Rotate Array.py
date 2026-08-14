# Given an array arr[]. 
# Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. 
# Do the mentioned change in the array in place.

# Note: Consider the array as circular.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        # Handle cases where d >= n
        d %= n
        
        # Helper function to reverse elements in-place between indices start and end
        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        # Step 1: Reverse the first d elements
        reverse(0, d - 1)
        # Step 2: Reverse the remaining (n - d) elements
        reverse(d, n - 1)
        # Step 3: Reverse the entire array
        reverse(0, n - 1)


# or

class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d %= n
        arr[:] = arr[d:] + arr[:d]