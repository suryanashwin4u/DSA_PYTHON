# Given a string s, convert the characters of the string into the opposite case, i.e., 
# if a character is lowercase, then convert it into uppercase and vice versa. 

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def toggleCase(self, s: str) -> str:
        # Option 1: Built-in swapcase
        return s.swapcase()

# or
 
class Solution:
    def toggleCase(self, s: str) -> str:
        res = []
        for char in s:
            if char.isupper():
                res.append(char.lower())
            else:
                res.append(char.upper())
        return "".join(res)