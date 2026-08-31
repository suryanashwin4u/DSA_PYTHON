# Given an array prices[] of non-negative integers, representing the prices of the stocks on different days. 
# The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. 
# Here one transaction means 1 buy + 1 Sell. 
# If it is not possible to make a profit then return 0.

# Note: Stock must be bought before being sold.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update minimum purchase price seen so far
            if price < min_price:
                min_price = price
            # Calculate potential profit if sold today
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

