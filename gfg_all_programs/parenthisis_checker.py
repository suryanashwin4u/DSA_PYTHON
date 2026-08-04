class Solution:
    def isBalanced(self, s):
        stack = []
        match = {')':'(', '}':'{', ']':'['}

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack or stack[-1] != match[ch]:
                    return False
                stack.pop()

        return len(stack) == 0
