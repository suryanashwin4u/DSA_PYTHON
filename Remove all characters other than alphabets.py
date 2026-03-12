# Given a string S, remove all the characters other than the alphabets.

class Solution:
    def removeSpecialCharacter(self, S):
        result = ""
        
        for ch in S:
            if ch.isalpha():
                result += ch
        
        if result == "":
            return "-1"
        
        return result