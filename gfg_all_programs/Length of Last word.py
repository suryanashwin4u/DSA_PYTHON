# Given a string s consisting of upper/lower-case alphabets and empty space characters ‘ ‘. 
# The string may contain spaces at the end. 
# You will have return the length of last word which consists of alphabets only.

class Solution:
    def findLength(self, s):
        return len(s.strip().split()[-1])