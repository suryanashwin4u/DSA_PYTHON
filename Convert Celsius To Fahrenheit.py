# Given a temperature in celsius C. You need to convert the given temperature into Fahrenheit.
# Time Complexity: O(1)
# Auxiliary Space: O(1)

class Solution:
    def cToF(self, C):
        return (C * 9/5) + 32
