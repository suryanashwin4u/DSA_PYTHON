# Given a positive integer n, determine whether it is an Armstrong number or not.

# An Armstrong number is a number where, sum of each digit raised to the power digit count, is equal to the original number.

# Expected Complexities
# Time Complexity: O(d), where d is the number of digits in n
# Auxiliary Space: O(d)

class Solution:
    def armstrongNumber(self, n: int) -> bool:
        digits = str(n)
        power = len(digits)
        total = sum(int(d) ** power for d in digits)
        return total == n