# You are given an integer input N and 
# you have to find whether it is the sum or the difference of the integer 5. 
# (5+5, 5+5+5, 5-5,5-5-5+5+5…..)

class Solution:
    def isValid(self, N):
        return "YES" if N % 5 == 0 else "NO"