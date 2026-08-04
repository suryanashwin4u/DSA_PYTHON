# Your are given a number n . 
# The number is said to be a Spy number if the sum of all the digits is equal to the product of all digits. 
# Return true if number is Spy number, else false.

class Solution:
    def checkSpy(self, n):
        # Initialize sum of digits
        digit_sum = 0
        
        # Initialize product of digits
        digit_product = 1
        
        # Loop until all digits are processed
        while n > 0:
            # Extract last digit
            digit = n % 10
            
            # Add digit to sum
            digit_sum += digit
            
            # Multiply digit with product
            digit_product *= digit
            
            # Remove last digit
            n //= 10
        
        # Check if sum and product are equal
        return digit_sum == digit_product
