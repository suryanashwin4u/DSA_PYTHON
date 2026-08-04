# Given an array arr[] of integers and another integer target. 
# Determine if there exist two distinct indices such that the sum of their elements is equal to the target.

class Solution:
    def twoSum(self, arr, target):
        # Set to store elements seen so far
        seen = set()
        
        # Traverse through the array
        for num in arr:
            # Value needed to form the target sum
            required = target - num
            
            # If required value already exists, pair found
            if required in seen:
                return True
            
            # Otherwise, store current number
            seen.add(num)
        
        # No pair found
        return False


