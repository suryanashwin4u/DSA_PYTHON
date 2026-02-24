# Given a string S  and a character X, 
# the task is to find the last index (0 based indexing) of X in string S. 
# If no index found then the answer will be -1.

class Solution:
    def LastIndex(self, s, p):
        for i in range(len(s) - 1, -1, -1):
            if s[i] == p:
                return i
        return -1