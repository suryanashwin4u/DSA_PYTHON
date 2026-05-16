# Given a number n, if the number is between 1 and 10 both inclusive then return the number in words (Lower case English Alphabets) otherwise return "not in range".
# Note: After printing the required string, print a newline character.

# Time Complexity: O(1)
# Auxiliary Space: O(1)

# User function Template for python3
class Solution:
    def isInRange(self, N):
        match N:
            case 1:
                return "one"
            case 2:
                return "two"
            case 3:
                return "three"
            case 4:
                return "four"
            case 5:
                return "five"
            case 6:
                return "six"
            case 7:
                return "seven"
            case 8:
                return "eight"
            case 9:
                return "nine"
            case 10:
                return "ten"
            case _:
                return "not in range"