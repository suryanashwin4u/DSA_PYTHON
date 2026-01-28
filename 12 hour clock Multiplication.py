# Given two positive integers num1 and num2, 
# the task is to find the product of the two numbers on a 12 hour clock rather than a number line.
# Note: Assume the Clock starts from 0 hour to 11 hours.

class Solution:
    def mulClock(self, num1, num2):
        # Multiply the two numbers
        product = num1 * num2
        
        # Return the result on a 12-hour clock
        return product % 12