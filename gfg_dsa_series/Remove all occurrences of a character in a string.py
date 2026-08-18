# Given a string s and a character c. 
# The task is to remove all the occurrences of the character in the string.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def removeCharacter(self, s, c):
        return s.replace(c, '')
    
# or

class Solution:
    def removeCharacter(self, s, c):
        return ''.join([char for char in s if char != c])