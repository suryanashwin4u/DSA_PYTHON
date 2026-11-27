# Given an integer n, print all numbers from n to 1 in decreasing order, separated by spaces, without using any loops.
# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:
    def printNos(self, n: int) -> None:
        if n <= 0:
            return

        print(n, end=" ")
        self.printNos(n - 1)