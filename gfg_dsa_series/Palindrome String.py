# Given a string s, return true if the string is a palindrome. Otherwise, return false.
# A string is considered a palindrome if it reads the same forwards and backwards.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

# or
  
class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]