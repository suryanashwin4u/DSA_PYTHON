# Given two numbers n and s , 
# find the largest number that can be formed with n digits and whose sum of digits should be equals to s. 
# Return -1 if it is not possible.
# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def findLargest(self, n, s):

        # impossible case
        if s > 9 * n:
            return "-1"

        # special case
        if s == 0:
            return "0" if n == 1 else "-1"

        ans = ""

        for i in range(n):

            digit = min(9, s)

            ans += str(digit)

            s -= digit

        return ans