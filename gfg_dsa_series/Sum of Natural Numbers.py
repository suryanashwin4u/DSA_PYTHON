# Given an integer n, compute the sum of all natural numbers from 1 to n (inclusive). 
# If n is 0, the sum should be 0.

# Time Complexity: O(1)
# Auxiliary Space: O(1)

n = int(input())

# code here
sum = n * (n + 1) // 2
print(sum)

# | Line | Code                     | Time Complexity | Space Complexity | Explanation                                          |
# | ---- | ------------------------ | --------------- | ---------------- | ---------------------------------------------------- |
# | 1    | `n = int(input())`       | **O(1)**        | **O(1)**         | Reads one integer from input.                        |
# | 3    | `sum = n * (n + 1) // 2` | **O(1)**        | **O(1)**         | Performs a constant number of arithmetic operations. |
# | 4    | `print(sum)`             | **O(1)**        | **O(1)**         | Prints the result.                                   |
