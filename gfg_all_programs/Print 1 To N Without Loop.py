# You are given an integer n. 
# You have  to print all numbers from 1 to n.
# Note: You must use recursion only, 
# and print all numbers from 1 to n in a single line, separated by spaces.
# printNos(5)
#  → printNos(4)
#    → printNos(3)
#      → printNos(2)
#        → printNos(1)
#          → printNos(0)  // stops here


class Solution:
    def printNos(self, n):
        # Base case
        if n == 0:
            return
        
        # Recursive call
        self.printNos(n - 1)
        
        # Print number
        print(n, end=" ")


