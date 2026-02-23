# You are given two long numbers N1 and N2 in a string. 
# You need to find out if the product of these numbers generate an even number or an odd number, 
# If it is an even number print 1 else print 0.

# User function Template for python3

class Solution:
    def EvenOdd(self, n1, n2):
        if (n1 % 2 == 0) or (n2 % 2 == 0):
            return 1
        return 0