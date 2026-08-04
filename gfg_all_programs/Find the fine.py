# Given an array of car numbers car[], an array of penalties fine[], and an integer value date. 
# The task is to find the total fine which will be collected on the given date. 
# The fine is collected from odd-numbered cars on even dates and vice versa.

class Solution:
    def totalFine(self, date, car, fine):
        total = 0
        
        for i in range(len(car)):
            # Collect fine when parity is opposite
            if car[i] % 2 != date % 2:
                total += fine[i]
        
        return total