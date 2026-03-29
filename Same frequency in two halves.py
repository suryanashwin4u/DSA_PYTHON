# Given a string S, find whether it fulfills the following criteria. 
# When split from the middle, the string should give two halves having the same characters and same frequency of each character. 
# If the number of characters in the string is odd, ignore the middle character.

class Solution:
    def passed(self, s):
        n = len(s)
        
        freq = [0] * 26
        
        # Count first half
        for i in range(n // 2):
            freq[ord(s[i]) - ord('a')] += 1
        
        # Count second half
        start = (n // 2) + (n % 2)  # skip middle if odd
        
        for i in range(start, n):
            freq[ord(s[i]) - ord('a')] -= 1
        
        # Check all zero
        for x in freq:
            if x != 0:
                return False
        
        return True