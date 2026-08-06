# You are given a 3-digit number n, Find whether it is an Armstrong number or not.

# An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 
# 371 is an Armstrong number since 33 + 73 + 13 = 371. 

# Time Complexity: O(1)
# Auxiliary Space: O(1)

class Solution:
    def armstrongNumber(self, n: int) -> bool:
        # Extract the individual digits for a 3-digit number
        d1 = n // 100
        d2 = (n // 10) % 10
        d3 = n % 10
        
        # Check if the sum of the cubes of the digits equals the original number
        return (d1**3 + d2**3 + d3**3) == n
