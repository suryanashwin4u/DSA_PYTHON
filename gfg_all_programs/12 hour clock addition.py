# Given two positive integers num1 and num2, 
# the task is to find the sum of the two numbers on a 12 hour clock rather than a number line.

class Solution:
    def clockSum(self, num1, num2):
        # Add both numbers
        total = num1 + num2
        
        # Return result in 12-hour clock format
        return total % 12