# Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.
# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def utility(self, x):
        while x >= 0:
            print(x, end=" ")
            x -= 1