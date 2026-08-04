# Given a alphanumeric string S, extract maximum numeric value from S.

class Solution:
    def extractMaximum(self, S):
        max_num = -1
        current = 0
        found = False
        
        for ch in S:
            if ch.isdigit():
                current = current * 10 + int(ch)
                found = True
            else:
                if found:
                    max_num = max(max_num, current)
                    current = 0
                    found = False
        
        # check last number
        if found:
            max_num = max(max_num, current)
        
        return max_num