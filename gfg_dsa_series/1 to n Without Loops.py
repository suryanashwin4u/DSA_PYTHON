# Given an positive integer n, print numbers from 1 to n without using loops.
# Implement the function printTillN() to print the numbers from 1 to n as space-separated integers.

# Time Complexity: O(n)
# Auxiliary Space: O(n)


class Solution:
    def printTillN(self, n):
        # Base case: stop recursion when n reaches 0
        if n == 0:
            return
        
        # Recursive call to print numbers from 1 to n-1 first
        self.printTillN(n - 1)
        
        # Print current n followed by a space
        print(n, end=" ")