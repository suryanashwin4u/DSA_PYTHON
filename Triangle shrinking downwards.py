# Given a string of a constant length, print a triangle out of it. 
# The triangle should start with the given string and keeps shrinking downwards by removing one character from the begining of the string. 
# The spaces on the left side of the triangle should be replaced with dot character.

class Solution:
    def triDownwards(self, S):
        n = len(S)
        result = []  # to store each line of the triangle

        for i in range(n):
            # i dots + substring from index i to end
            line = '.' * i + S[i:]
            result.append(line)

        # join all lines into a single string
        return ''.join(result)