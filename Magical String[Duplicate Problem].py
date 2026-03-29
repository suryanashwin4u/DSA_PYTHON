# You are given a string S, convert it into a magical string.
# A string can be made into a magical string 
# if the alphabets are swapped in the given manner: a->z or z->a, b->y or y->b, and so on.  
# Note: All the alphabets in the string are in lowercase.

class Solution:
    def magicalString(self, S):
        result = []
        
        for ch in S:
            mirror = chr(ord('z') - (ord(ch) - ord('a')))
            result.append(mirror)
        
        return "".join(result)