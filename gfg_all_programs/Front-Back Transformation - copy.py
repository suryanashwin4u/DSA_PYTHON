# Given a string S, consisting only of english alphabets, 
# replace all the alphabets with the alphabets occuring at the same position 
# when counted in reverse order of alphabets. 
# For example, 'a' would be replaced by 'z', 'b' by 'y', 'c' by 'x' and so on. 
# Any capital letters would be replaced by capital letters only.

class Solution:
    def convert(self, s):
        result = []

        for ch in s:
            # if lowercase letter
            if 'a' <= ch <= 'z':
                result.append(chr(ord('z') - (ord(ch) - ord('a'))))
            
            # if uppercase letter
            elif 'A' <= ch <= 'Z':
                result.append(chr(ord('Z') - (ord(ch) - ord('A'))))

        return "".join(result)