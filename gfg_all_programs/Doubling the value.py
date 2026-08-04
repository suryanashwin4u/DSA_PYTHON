# Given an array arr and an integer b, traverse the array (from the beginning) and if the element in array is b, 
# double b and continue traversal. 
# Find the value of b after the complete traversal.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def solve(self, b: int, arr: list[int]) -> int:
        for x in arr:
            if x == b:
                b *= 2
        return b

