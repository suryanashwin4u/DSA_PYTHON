# Given an array arr of integers. 
# First sort the array then find 
# whether three numbers are such that the 
# sum of two elements equals the third element.

class Solution:
    def findTriplet(self, arr):
        # Step 1: Sort the array
        # Sorting helps us apply the two-pointer technique
        arr.sort()
        n = len(arr)

        # Step 2: Fix the third element (largest element of the triplet)
        # We start from the last index and move backwards
        for k in range(n - 1, 1, -1):

            # Step 3: Initialize two pointers
            # i -> start of array
            # j -> just before k
            i = 0
            j = k - 1

            # Step 4: Use two-pointer approach
            while i < j:
                # Calculate sum of two elements
                s = arr[i] + arr[j]

                # If sum equals the third element
                if s == arr[k]:
                    return True   # Triplet found

                # If sum is smaller, move left pointer to right
                elif s < arr[k]:
                    i += 1

                # If sum is greater, move right pointer to left
                else:
                    j -= 1

        # Step 5: If no such triplet is found
        return False