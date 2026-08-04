# Given a number n, print pyramid pattern with n lines.

# Time Complexity: O(n^2)
# Auxiliary Space: O(1)

n = int(input())

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()

# | Line No. | Code                         | Time Complexity  | Space Complexity | Explanation                               |
# | -------: | ---------------------------- | ---------------- | ---------------- | ----------------------------------------- |
# |        1 | `n = int(input())`           | **O(1)**         | **O(1)**         | Read input integer.                       |
# |        2 | `for i in range(n):`         | **O(n)**         | **O(1)**         | Outer loop executes `n` times.            |
# |        3 | `for j in range(n - i - 1):` | **O(n - i - 1)** | **O(1)**         | Prints leading spaces for each row.       |
# |        4 | `print(" ", end="")`         | **O(1)**         | **O(1)**         | Prints one space. Executed `n-i-1` times. |
# |        5 | `for j in range(2 * i + 1):` | **O(2i + 1)**    | **O(1)**         | Prints stars for current row.             |
# |        6 | `print("*", end="")`         | **O(1)**         | **O(1)**         | Prints one star. Executed `2i+1` times.   |
# |        7 | `print()`                    | **O(1)**         | **O(1)**         | Moves to the next line.                   |

