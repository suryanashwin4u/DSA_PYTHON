# Given two positive integers num1 and num2, 
# subtract num2 from num1 on a 12 hour clock rather than a number line.
# Note: Assume the Clock starts from 0 hour to 11 hours.

class Solution:
    def subClock(self, num1, num2):
        # Subtract num2 from num1
        diff = num1 - num2
        
        # Take modulo 12 to wrap around the clock
        # Python % already gives non-negative result
        result = diff % 12
        
        return result