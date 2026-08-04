# Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.
# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def utility(self, x):
        while x >= 0:
            print(x, end=" ")
            x -= 1

# | Line | Code                    | Time Complexity        | Space Complexity | Explanation                                                                                |
# | ---- | ----------------------- | ---------------------- | ---------------- | ------------------------------------------------------------------------------------------ |
# | 1    | `class Solution:`       | **O(1)**               | **O(1)**         | Class declaration.                                                                         |
# | 2    | `def utility(self, x):` | **O(1)**               | **O(1)**         | Function definition.                                                                       |
# | 3    | `while x >= 0:`         | **O(x + 1)**           | **O(1)**         | Condition is checked `x + 2` times (including the final false check), so overall **O(x)**. |
# | 4    | `print(x, end=" ")`     | **O(1)** per iteration | **O(1)**         | Prints one integer each iteration. Executed `x + 1` times.                                 |
# | 5    | `x -= 1`                | **O(1)** per iteration | **O(1)**         | Decrements `x`. Executed `x + 1` times.                                                    |

