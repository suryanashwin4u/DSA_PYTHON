# Given a string s, extract all the integers from s.

class Solution:
    def extractIntegerWords(self, s):
        result = []
        temp = ""

        for ch in s:
            if ch.isdigit():
                temp += ch
            else:
                if temp:
                    result.append(temp)
                    temp = ""

        # For number at the end of string
        if temp:
            result.append(temp)

        return result