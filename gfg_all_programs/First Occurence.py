# Given two strings txt and pat, 
# return the 0-based index of the first occurrence of the substring pat in txt. 
# If pat is not found, return -1.
# Note: You are not allowed to use the inbuilt function.

class Solution:
    def firstOccurence(self, txt, pat):
        n = len(txt)
        m = len(pat)

        # Loop through txt
        for i in range(n - m + 1):
            j = 0
            
            # Compare characters of pat with txt
            while j < m and txt[i + j] == pat[j]:
                j += 1
            
            # If full pattern matched
            if j == m:
                return i
        
        return -1