# Given a positive integer n, determine whether it is odd or even. 
# Return true if the number is even and false if the number is odd.

# Time Complexity: O(1)
# Auxiliary Space: O(1)

class Solution:
    def isEven(self, n):
        return n % 2 == 0
    
# | Line | Code                   | Time Complexity | Space Complexity | Explanation                                              |
# | ---- | ---------------------- | --------------- | ---------------- | -------------------------------------------------------- |
# | 1    | `class Solution:`      | O(1)            | O(1)             | Defines the class.                                       |
# | 2    | `def isEven(self, n):` | O(1)            | O(1)             | Defines the function.                                    |
# | 3    | `return n % 2 == 0`    | O(1)            | O(1)             | Modulo operation and comparison both take constant time. |