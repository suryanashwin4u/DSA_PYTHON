# Given an integer N represented in the form of a string, 
# remove consecutive repeated digits from it.

class Solution:
    def modify(self, N):
        s = str(N)
        ans = s[0]
        
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                ans += s[i]
                
        return int(ans)

