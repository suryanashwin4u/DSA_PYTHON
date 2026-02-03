# Given a string consisting of lowercase English alphabets, 
# reverse only the vowels present in it and print the resulting string.

# User function Template for python3

class Solution:
    def modify(self, s):
        # Convert string to list because strings are immutable in Python
        s = list(s)

        # Set of vowels for O(1) lookup
        vowels = set('aeiou')

        # Two pointers:
        # left  -> starts from beginning of string
        # right -> starts from end of string
        left = 0
        right = len(s) - 1

        # Loop until the two pointers cross each other
        while left < right:

            # If left character is NOT a vowel, move left pointer forward
            if s[left] not in vowels:
                left += 1

            # If right character is NOT a vowel, move right pointer backward
            elif s[right] not in vowels:
                right -= 1

            # If both characters are vowels, swap them
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        # Convert list back to string and return result
        return ''.join(s)