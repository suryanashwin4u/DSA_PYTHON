# Given an integer n. Write a program to find last digit of the number.

class Solution:
    def utility(self, n):
        ans = abs(n) % 10
        print(ans)
