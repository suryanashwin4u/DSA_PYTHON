# You are given a string s. You need to find if the string is a panagram or not.
# Note: A panagram contains all the letters of english alphabet at least once.

class Solution:
    def isPanagram(self, s):
        seen = [False] * 26
        
        for ch in s:
            if ch.isalpha():
                ch = ch.lower()
                seen[ord(ch) - ord('a')] = True
        
        return all(seen)
