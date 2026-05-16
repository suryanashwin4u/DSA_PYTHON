# Given a string s, and a pattern p. 
# You need to find if p exists in s or not and return the starting index of p in s. 
# If p does not exist in s then -1 will be returned.
# Here p and s both are case-sensitive.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

def findPattern(s, p):
    return s.find(p)