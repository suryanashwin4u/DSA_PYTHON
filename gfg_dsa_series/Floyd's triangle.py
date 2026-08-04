# Given a number n, print Floyd's triangle with n lines.

# Floyd’s Triangle is a pattern of consecutive natural numbers arranged in rows, 
# where the i-th row contains i numbers.

# Time Complexity: O(n^2)
# Auxiliary Space: O(1)

n = int(input())

num = 1

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()


# | Line | Code                        | Time Complexity              | Space Complexity | Explanation                                          |
# | ---- | --------------------------- | ---------------------------- | ---------------- | ---------------------------------------------------- |
# | 1    | `n = int(input())`          | **O(1)**                     | **O(1)**         | Reads one integer input.                             |
# | 2    | `num = 1`                   | **O(1)**                     | **O(1)**         | Variable initialization.                             |
# | 3    | `for i in range(1, n + 1):` | **O(n)**                     | **O(1)**         | Outer loop executes `n` times.                       |
# | 4    | `for j in range(1, i + 1):` | **O(i)** per outer iteration | **O(1)**         | Inner loop runs `i` times for row `i`.               |
# | 5    | `print(num, end=" ")`       | **O(1)**                     | **O(1)**         | Prints one number. Executed `n(n+1)/2` times.        |
# | 6    | `num += 1`                  | **O(1)**                     | **O(1)**         | Constant-time increment.                             |
# | 7    | `print()`                   | **O(1)**                     | **O(1)**         | Prints a newline after each row. Executes `n` times. |
