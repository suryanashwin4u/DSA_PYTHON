# Given a string s consisting of lowercase English Letters. 
# return the first non-repeating character in s. 
# If there is no non-repeating character, return '$'.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def nonRepeatingChar(self, s: str) -> str:
        # Count frequency of each character
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # Find the first character with frequency 1
        for char in s:
            if freq[char] == 1:
                return char
                
        return '$'
    
# or

class Solution:
    def nonRepeatingChar(self, s: str) -> str:
        freq = [0] * 26
        
        for char in s:
            freq[ord(char) - ord('a')] += 1
            
        for char in s:
            if freq[ord(char) - ord('a')] == 1:
                return char
                
        return '$'
