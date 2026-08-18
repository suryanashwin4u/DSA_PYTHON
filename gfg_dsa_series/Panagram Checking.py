# Given a string s, check if it is a "Panagram" or not.  
# A "Panagram" is a sentence containing every letter in the English Alphabet either in lowercase or Uppercase.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def checkPangram(self, s: str) -> bool:
        # Filter only alphabetic characters, convert to lowercase, and collect unique characters
        found_letters = {char.lower() for char in s if char.isalpha()}
        
        # Check if all 26 letters of the English alphabet are present
        return len(found_letters) == 26
