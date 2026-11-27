# Given a number n. Print Hollow Diamond Pattern with n lines.
# Note: There is a space between two adjacent stars (*) in the pattern.

# Expected Complexities
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)


class Solution:
    def printPat(self, n):
        total_lines = 2 * n - 1

        for row in range(total_lines):
            dist = abs((n - 1) - row)
            step = (n - 1) - dist  # 0 at top/bottom tip, n-1 at widest row

            # Leading spaces match expected left margin
            leading_spaces = " " * dist

            if step == 0:
                print(leading_spaces + "*")
            else:
                # Gap grows by 4 per step: 3, 7, 11, ...
                inner_gap = " " * (4 * step - 1)
                print(leading_spaces + "*" + inner_gap + "*")