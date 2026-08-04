# Given a number n, determine whether it is a prime number or not.
# Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

# Time Complexity: O(sqrt(n))
# Auxiliary Space: O(1)

class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False

        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1

        return True

# | Line | Code                    | Time Complexity    | Space Complexity | Explanation                               |
# | ---- | ----------------------- | ------------------ | ---------------- | ----------------------------------------- |
# | 1    | `class Solution:`       | O(1)               | O(1)             | Class declaration.                        |
# | 2    | `def isPrime(self, n):` | O(1)               | O(1)             | Function definition.                      |
# | 3    | `if n <= 1:`            | O(1)               | O(1)             | Single comparison.                        |
# | 4    | `return False`          | O(1)               | O(1)             | Constant-time return.                     |
# | 5    | `i = 2`                 | O(1)               | O(1)             | Variable initialization.                  |
# | 6    | `while i * i <= n:`     | **O(√n)**          | O(1)             | Loop executes at most √n−1 iterations.    |
# | 7    | `if n % i == 0:`        | O(1) per iteration | O(1)             | One modulo and comparison each iteration. |
# | 8    | `return False`          | O(1)               | O(1)             | Executes once when a divisor is found.    |
# | 9    | `i += 1`                | O(1) per iteration | O(1)             | Increment operation.                      |
# | 10   | `return True`           | O(1)               | O(1)             | Executes if no divisor exists.            |