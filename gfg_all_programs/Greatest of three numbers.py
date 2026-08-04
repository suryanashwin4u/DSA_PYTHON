# Given three numbers a, b and c. Find the greatest number among them.
# Time Complexity: O(1)
# Auxiliary Space: O(1)

class Solution:
    def greatestOfThree(self, a, b, c):
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        else:
            return c
        

class Solution:
    def greatestOfThree(self, a, b, c):
        return max(a, b, c)