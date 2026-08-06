# Given a number n. Print Hollow Diamond Pattern with n lines.
# Note: There is a space between two adjacent stars (*) in the pattern.

# Time Complexity: O(n^2)
# Auxiliary Space: O(1)

class Solution:
    def printPat(self, n):
        # Top half (including center row)
        for i in range(n):
            spaces = '  ' * (n - 1 - i)
            if i == 0:
                print(spaces + '*')
            else:
                inner_spaces = ' ' * (4 * i - 1)
                print(spaces + '*' + inner_spaces + '*')

        # Bottom half
        for i in range(n - 2, -1, -1):
            spaces = '  ' * (n - 1 - i)
            if i == 0:
                print(spaces + '*')
            else:
                inner_spaces = ' ' * (4 * i - 1)
                print(spaces + '*' + inner_spaces + '*')
