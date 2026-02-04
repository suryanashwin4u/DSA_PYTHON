# Given an array arr[] and two elements x and y, 
# return the element that occurs more frequently. 
# If both elements have the same frequency, return the smaller one.

class Solution:
    def moreFrequent(self, arr, x, y):
        # Initialize counters for x and y
        count_x = 0
        count_y = 0

        # Traverse the array once
        for num in arr:
            if num == x:
                count_x += 1     # Increment count if element is x
            elif num == y:
                count_y += 1     # Increment count if element is y

        # Compare frequencies
        if count_x > count_y:
            return x             # x appears more times
        elif count_y > count_x:
            return y             # y appears more times
        else:
            return min(x, y)     # Same frequency → return smaller number


