# Given a string s, remove all the spaces from the string and return the modified string.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def removeSpaces(self, s: str) -> str:
        return s.replace(" ", "")