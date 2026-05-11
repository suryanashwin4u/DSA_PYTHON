# Given a string s1 and another string s2. 
# Find the minimum index of the character in s1 that is also present in s2. 
# if no character common in both then return -1.
# Time Complexity: O(n)
# Space Complexity: O(1) (only 26 lowercase letters possible)

class Solution:
    def minIndexChar(self, s1, s2):
        
        # store characters of s2 in a set
        st = set(s2)
        
        # check characters of s1
        for i in range(len(s1)):
            if s1[i] in st:
                return i
        
        return -1