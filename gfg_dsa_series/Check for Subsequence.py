# Given two strings s1 and s2. You have to check that s1 is a subsequence of s2 or not.
# Note: A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def isSubSeq(self, s1, s2):
        i, j = 0, 0
        n, m = len(s1), len(s2)
        
        while i < n and j < m:
            if s1[i] == s2[j]:
                i += 1
            j += 1
            
        return i == n

