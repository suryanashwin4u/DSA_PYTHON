# Print numbers from n to 1 (space separated) without the help of loops.

# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:
    def printNos(self, n):
        # Base case: stop when n reaches 0
        if n == 0:
            return
        
        # Print current number followed by a space
        print(n, end=" ")
        
        # Recursive call with n - 1
        self.printNos(n - 1)

