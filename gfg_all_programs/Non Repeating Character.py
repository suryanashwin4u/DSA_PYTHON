# Given a string s consisting of lowercase English Letters. 
# return the first non-repeating character in s. 
# If there is no non-repeating character, return '$'.

class Solution:
    def nonRepeatingChar(self, s):
        freq = [0] * 26
        
        # Count frequency
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        # Find first non-repeating character
        for ch in s:
            if freq[ord(ch) - ord('a')] == 1:
                return ch
        
        return '$'
