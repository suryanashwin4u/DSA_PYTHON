# Given an unsorted array arr[ ] having both negative and positive integers. 
# Place all negative elements at the end of the array without changing the order of positive elements and negative elements.
# Note: Don't return any array, just in-place on the array.

# Complexity
# Time: O(n)
# Space: O(n)

class Solution:
    def segregateElements(self, arr):
        positive = []
        negative = []
        
        for num in arr:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)
        
        # modify original array in-place
        arr[:] = positive + negative