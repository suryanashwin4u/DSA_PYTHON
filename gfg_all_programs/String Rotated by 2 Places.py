# Given two strings s1 and s2. 
# Return true if the string s2 can be obtained by rotating (in any direction) string s1 by exactly 2 places, otherwise, false.
# Note: Both rotations should be performed in same direction chosen initially.

class Solution:
    def isRotated(self, s1, s2):

        if len(s1) != len(s2):
            return False

        # Edge case
        if len(s1) <= 2:
            return s1 == s2

        # Left rotation by 2
        left = s1[2:] + s1[:2]

        # Right rotation by 2
        right = s1[-2:] + s1[:-2]

        return s2 == left or s2 == right