# Given an integer n. Write a program to find last digit of the number.
# Time Complexity: O(1)
# Auxiliary Space: O(1)

class Solution:
    def utility(self, n):
        ans = abs(n) % 10
        print(ans)
