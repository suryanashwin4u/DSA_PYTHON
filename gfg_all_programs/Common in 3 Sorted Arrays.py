# Given three sorted arrays in non-decreasing order, 
# print all common elements in non-decreasing order across these arrays. 
# If there are no such elements return an empty array. 
# In this case, the output will be -1.
# Note: can you handle the duplicates without using any additional Data Structure?

class Solution:
    def commonElements(self, arr1, arr2, arr3):

        # Three pointers for three arrays
        i = 0
        j = 0
        k = 0

        # List to store common elements
        result = []

        # Loop until any one array ends
        while i < len(arr1) and j < len(arr2) and k < len(arr3):

            # If all three elements are equal
            if arr1[i] == arr2[j] and arr2[j] == arr3[k]:

                # To avoid duplicates in result array
                if not result or result[-1] != arr1[i]:
                    result.append(arr1[i])

                # Move all pointers forward
                i += 1
                j += 1
                k += 1

            # If element in arr1 is smallest, move i
            elif arr1[i] < arr2[j]:
                i += 1

            # If element in arr2 is smallest, move j
            elif arr2[j] < arr3[k]:
                j += 1

            # Otherwise, move k
            else:
                k += 1

        # If no common element found
        if not result:
            return [-1]

        return result
