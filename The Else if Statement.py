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