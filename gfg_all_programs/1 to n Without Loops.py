# Given an positive integer n, print numbers from 1 to n without using loops.

# Implement the function printTillN() to print the numbers from 1 to n as space-separated integers.

# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:
    def printTillN(self, n):
        
        if n == 0:
            return

        self.printTillN(n - 1)

        print(n, end=" ")