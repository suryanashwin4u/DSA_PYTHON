# A number n is said to be a Buzz Number if it ends with 7 OR is divisible by 7. 
# The task is to check whether the given number is Buzz number or not. 
# Return true if n is a Buzz Number else return false.

class Solution:
    def isBuzz(self, n):
        # Check if number ends with 7 OR divisible by 7
        return n % 10 == 7 or n % 7 == 0
