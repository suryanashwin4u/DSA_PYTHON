# You are given a binary number as a string of characters ('0' and '1'). 
# Your task is to determine whether this binary number is divisible by 3. 
# Note: Try to accomplish this using a single traversal of the input binary string.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

#User function Template for python3
class Solution:
    def isDivisible(self, s):
        
        rem = 0
        
        for bit in s:
            rem = (rem * 2 + int(bit)) % 3
        
        return rem == 0

# or
# shortest method
class Solution:
    def isDivisible(self, s):
        return int(s, 2) % 3 == 0