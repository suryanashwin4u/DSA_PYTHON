# Calculate the amount for given principal amount P , time T(in years), compounded N times in a year at rate R. 
# Calculate floor of future value of given principal amount

import math

class Solution:
    def getCompundInterest(self, P, T, N, R):
        # Calculate the rate per compounding period
        rate_per_period = R / (100 * N)
        
        # Total number of compounding periods
        total_periods = N * T
        
        # Apply compound interest formula
        amount = P * ((1 + rate_per_period) ** total_periods)
        
        # Return the floor value of the amount
        return math.floor(amount)