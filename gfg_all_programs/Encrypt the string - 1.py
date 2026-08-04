# Every substring of identical letters is replaced by a single instance of that letter 
# followed by the number of occurrences of that letter. 
# Then, the string thus obtained is further encrypted by reversing it.

class Solution:
    def encryptString(self, s):
        res = ""
        count = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                res += s[i-1] + str(count)
                count = 1
        
        res += s[-1] + str(count)
        
        return res[::-1]
