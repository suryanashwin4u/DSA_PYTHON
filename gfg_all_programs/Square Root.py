# Given a positive integer n, 
# find the square root of n. 
# If n is not a perfect square, 
# then return the floor value.
# Floor value of any number is the greatest Integer which is less than or equal to that number.

class Solution:
    def floorSqrt(self, n):
        # Base cases
        if n == 0 or n == 1:
            return n
        
        low = 1
        high = n
        ans = 0  # to store floor value
        
        while low <= high:
            mid = (low + high) // 2
            
            # If perfect square
            if mid * mid == n:
                return mid
            
            # If mid^2 is smaller, move right
            elif mid * mid < n:
                ans = mid        # store possible answer
                low = mid + 1
            
            # If mid^2 is greater, move left
            else:
                high = mid - 1
        
        return ans