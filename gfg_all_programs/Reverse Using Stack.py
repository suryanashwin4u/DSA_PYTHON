# You are given a string s , the task is to reverse the string using stack.
# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:
    def reverse(self, s: str) -> str:
        stack = []

        # push all characters into stack
        for ch in s:
            stack.append(ch)

        ans = ""
        
        # pop characters from stack
        while stack:
            ans += stack.pop()

        return ans