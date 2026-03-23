# Given a string, say S, print it in reverse manner eliminating the repeated characters and spaces.

class Solution:
    def reverseString(self, s):
        seen = set()
        result = []

        # traverse from right to left
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ' and s[i] not in seen:
                seen.add(s[i])
                result.append(s[i])

        return ''.join(result)