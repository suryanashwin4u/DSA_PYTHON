# Given two strings S1 and S2 . Return "1" if both strings are anagrams otherwise return "0" .

# Note: An anagram of a string is another string with exactly the same quantity of each character in it, in any order.

class Solution:
    def areAnagram(self, S1, S2):
        # If lengths are different, cannot be anagram
        if len(S1) != len(S2):
            return "0"
        
        # Frequency array for 26 lowercase letters
        freq = [0] * 26
        
        # Count characters in S1
        for ch in S1:
            freq[ord(ch) - ord('a')] += 1
        
        # Subtract counts using S2
        for ch in S2:
            freq[ord(ch) - ord('a')] -= 1
        
        # If all counts are zero → anagram
        for count in freq:
            if count != 0:
                return "0"
        
        return "1"