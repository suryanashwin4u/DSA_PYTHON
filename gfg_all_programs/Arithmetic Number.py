# Given three integers  'a' denotes the first term of an arithmetic sequence, 
# 'c' denotes the common difference of an arithmetic sequence and an integer 'b'. 
# you need to tell whether 'b' exists in the arithmetic sequence or not. 
# Return 1 if b is present in the sequence. Otherwise, returns 0.

#User function Template for python3

class Solution:
    def inSequence(self, a, b, c):

        # When common difference is 0
        if c == 0:
            return 1 if a == b else 0

        # Check if b exists in AP
        if (b - a) % c == 0 and (b - a) // c >= 0:
            return 1

        return 0