# Given two strings S1 and S2 as input, 
# the task is to merge them alternatively i.e. 
# the first character of S1 then the first character of S2 and so on till the strings end.
# NOTE: Add the whole string if other string is empty.

# User function Template for python3

class Solution:
    def merge(self, S1, S2):
        result = ""
        for i in range(max(len(S1), len(S2))):
            if i < len(S1):
                result += S1[i]
            if i < len(S2):
                result += S2[i]
        return result
