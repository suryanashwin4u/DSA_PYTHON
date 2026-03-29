# Given a floating point number in string format s, check whether it is even or odd.

class Solution:
    def isEven(self, s, n):
        # Traverse from end
        for i in range(n - 1, -1, -1):
            if s[i] == '.':
                continue
            if s[i] == '0':
                continue
            
            # Check if digit is even
            return int(s[i]) % 2 == 0
        
        return False