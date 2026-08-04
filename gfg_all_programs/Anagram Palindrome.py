# Given a string S, Check if characters of the given string can be rearranged to form a palindrome.
# Note: You have to return 1 if it is possible to convert the given string into palindrome else return 0. 

class Solution:
    def isPossible(self, S):
        freq = {}
        
        # Count frequency of each character
        for ch in S:
            freq[ch] = freq.get(ch, 0) + 1
        
        odd_count = 0
        
        # Count characters with odd frequency
        for count in freq.values():
            if count % 2 != 0:
                odd_count += 1
                if odd_count > 1:
                    return 0
        
        return 1
