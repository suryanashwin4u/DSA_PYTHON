# Given two strings s1 and s2 consisting of only lowercase English letters and of equal length, check if these two strings are isomorphic to each other.
# If the characters in s1 can be changed to get s2, then two strings, s1 and s2 are isomorphic. A character must be completely swapped out for another character while maintaining the order of the characters. 
# A character may map to itself, but no two characters may map to the same character.
# Time Complexity: O(n)
# Auxiliary Space: O(1)


class Solution:
    def areIsomorphic(self, s1, s2):
        m1 = {}
        m2 = {}
        
        for i in range(len(s1)):
            c1 = s1[i]
            c2 = s2[i]
            
            if c1 in m1:
                if m1[c1] != c2:
                    return False
            else:
                m1[c1] = c2
            
            if c2 in m2:
                if m2[c2] != c1:
                    return False
            else:
                m2[c2] = c1
        
        return True