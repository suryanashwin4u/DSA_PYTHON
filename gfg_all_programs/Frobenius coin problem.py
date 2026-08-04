# Given two coins of denominations X and Y respectively, 
# find the largest amount that cannot be obtained using these two coins 
# (assuming infinite supply of coins) followed by the total number of such non obtainable amounts.

import math

class Solution:
    def frobenius(self, X, Y):
        # Step 1: Check GCD of X and Y
        # If gcd is not 1, infinite values cannot be formed
        if math.gcd(X, Y) != 1:
            return [-1]

        # Step 2: Largest amount that cannot be obtained
        # Formula: X*Y - X - Y
        largest_not_possible = X * Y - X - Y

        # Step 3: Total number of non-obtainable amounts
        # Formula: (X-1)*(Y-1)//2
        total_not_possible = (X - 1) * (Y - 1) // 2

        # Step 4: Return result as a list
        return [largest_not_possible, total_not_possible]
