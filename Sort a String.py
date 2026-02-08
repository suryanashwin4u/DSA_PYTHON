# Given a string consisting of lowercase letters, arrange all its letters in ascending order. 

class Solution:
    def sort(self, s):
        # Convert string to list and sort characters
        sorted_chars = sorted(s)
        
        # Join the sorted characters back into a string
        return ''.join(sorted_chars)