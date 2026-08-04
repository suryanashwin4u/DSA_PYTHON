# Given a number, you have to use if, else if, else conditional statements according to the following:
# if number is greater than 100: Print "Big" (without quotes)
# else if number is smaller than 10: Print "Small" (without quotes)
# else: Print "Number" (without quotes) 

# Note: Ensure that the output includes a newline after every print statement.

# Time Complexity: O(1)
# Auxiliary Space: O(1)

class Solution:
    def utility(self, number):
        if number > 100:
            print("Big")
        elif number < 10:
            print("Small")
        else:
            print("Number")


# | Line | Code                         | Time Complexity | Space Complexity | Explanation                                              |
# | ---- | ---------------------------- | --------------- | ---------------- | -------------------------------------------------------- |
# | 1    | `class Solution:`            | **O(1)**        | **O(1)**         | Declares a class.                                        |
# | 2    | `def utility(self, number):` | **O(1)**        | **O(1)**         | Defines a function.                                      |
# | 3    | `if number > 100:`           | **O(1)**        | **O(1)**         | Performs one comparison.                                 |
# | 4    | `print("Big")`               | **O(1)**        | **O(1)**         | Prints a constant string.                                |
# | 5    | `elif number < 10:`          | **O(1)**        | **O(1)**         | Performs one comparison if the first condition is false. |
# | 6    | `print("Small")`             | **O(1)**        | **O(1)**         | Prints a constant string.                                |
# | 7    | `else:`                      | **O(1)**        | **O(1)**         | Control statement with no computation.                   |
# | 8    | `print("Number")`            | **O(1)**        | **O(1)**         | Prints a constant string.                                |
