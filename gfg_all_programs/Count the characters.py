# Given a string S. 
# Count the characters that have ‘N’ number of occurrences. 
# If a character appears consecutively it is counted as 1 occurrence.

class Solution:
    def getCount(self, S, N):
        # Dictionary to store count of each character
        # (after ignoring consecutive duplicates)
        freq = {}

        # Variable to track the previous character
        prev = None

        # Traverse the string character by character
        for ch in S:
            # Count only when current character is
            # different from the previous character
            if ch != prev:
                freq[ch] = freq.get(ch, 0) + 1
            
            # Update previous character
            prev = ch

        # Variable to store final answer
        count = 0

        # Count how many characters have exactly N occurrences
        for value in freq.values():
            if value == N:
                count += 1

        return count
