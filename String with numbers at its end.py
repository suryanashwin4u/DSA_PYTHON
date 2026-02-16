# Given string s that is appended with a number at last. 
# The task is to check whether the length of string 
# excluding that number is equal to that number.

class Solution:
    def isSame(self, s):
        i = 0
        while i < len(s) and not s[i].isdigit():
            i += 1
        
        if len(s[:i]) == int(s[i:]):
            return 1
        else:
            return 0
