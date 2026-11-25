# Given an array of positive integers arr[], return the second largest element from the array. 
# If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def getSecondLargest(self, arr):
        largest = -1
        second_largest = -1

        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num != largest and num > second_largest:
                second_largest = num

        return second_largest