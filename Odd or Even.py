# Given a positive integer n, 
# determine whether it is odd or even. 
# Return true if the number is even and false if the number is odd.

# Approach 1: Using Modulus Operator
class Solution:
    def isEven(self, n):
        # If remainder after dividing by 2 is zero, number is even
        if n % 2 == 0:
            return True
        else:
            return False

# Approach 2: Using Bit Manipulation
class Solution:
    def isEven(self, n):
        # Last bit of even number is always 0
        return (n & 1) == 0
