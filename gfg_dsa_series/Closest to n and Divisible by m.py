# Given two integers n and m (m != 0). 
# The problem is to find the number closest to n and divisible by m. 
# If there is more than one such number, then output the one having the maximum absolute value.

# Time Complexity: O(1)
# Auxiliary Space: O(1)

class Solution:

    def closestNumber(self, n, m):

        # find the multiplier
        mul = n // m

        # find the closest lower multiple to n
        low = mul * m

        # find the closest higher multiple
        high = (mul + 1) * m

        # compare the distances
        if abs(low - n) > abs(high - n):
            return high
        elif abs(low - n) < abs(high - n):
            return low
        else:
            return low if abs(low) > abs(high) else high
        
# | Line | Code                                           | Time Complexity | Space Complexity | Explanation                                              |
# | ---- | ---------------------------------------------- | --------------- | ---------------- | -------------------------------------------------------- |
# | 1    | `class Solution:`                              | **O(1)**        | **O(1)**         | Class declaration.                                       |
# | 2    | `def closestNumber(self, n, m):`               | **O(1)**        | **O(1)**         | Function definition.                                     |
# | 3    | `mul = n // m`                                 | **O(1)**        | **O(1)**         | Integer division.                                        |
# | 4    | `low = mul * m`                                | **O(1)**        | **O(1)**         | One multiplication.                                      |
# | 5    | `high = (mul + 1) * m`                         | **O(1)**        | **O(1)**         | One addition and one multiplication.                     |
# | 6    | `if abs(low - n) > abs(high - n):`             | **O(1)**        | **O(1)**         | Constant number of arithmetic and comparison operations. |
# | 7    | `return high`                                  | **O(1)**        | **O(1)**         | Return statement.                                        |
# | 8    | `elif abs(low - n) < abs(high - n):`           | **O(1)**        | **O(1)**         | Constant-time comparison.                                |
# | 9    | `return low`                                   | **O(1)**        | **O(1)**         | Return statement.                                        |
# | 10   | `else:`                                        | **O(1)**        | **O(1)**         | Branch selection.                                        |
# | 11   | `return low if abs(low) > abs(high) else high` | **O(1)**        | **O(1)**         | Two `abs()` calls, one comparison, one return.           |
