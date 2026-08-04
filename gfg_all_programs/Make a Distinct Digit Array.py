# Given an array nums of positive integers of size N. 
# Find all distinct digits present in nums.

class Solution:
    def common_digits(self, nums):
        digits = set()
        
        for num in nums:
            while num > 0:
                digits.add(num % 10)
                num //= 10
        
        return sorted(digits)