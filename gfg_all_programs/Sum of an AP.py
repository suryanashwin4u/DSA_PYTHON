# Given n, a and d as the number of terms, first term and common difference respectively of an Arthimetic Series. 
# Find the sum of the series upto nth term.

class Solution:
    def sum_of_ap(self, n, a, d):
        # Using formula: n/2 * (2a + (n-1)d)
        
        # Calculate the expression inside the bracket
        expr = 2 * a + (n - 1) * d
        
        # Multiply with n/2
        result = (n * expr) // 2   # use // to keep integer result
        
        return result