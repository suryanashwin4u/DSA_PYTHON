# You are given an array arr[] of non-negative numbers. 
# Each number tells you the maximum number of steps you can jump forward from that position.

# For example:

# If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
# If arr[i] = 0, you cannot jump forward from that position.
# Your task is to find the minimum number of jumps needed to move 
# from the first position in the array to the last position.

# Note:  Return -1 if you can't reach the end of the array.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # Edge cases
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1
        
        maxReach = arr[0]
        steps = arr[0]
        jumps = 1
        
        for i in range(1, n):
            
            # If we reached the end
            if i == n - 1:
                return jumps
            
            # Update max reach
            maxReach = max(maxReach, i + arr[i])
            
            # Use a step
            steps -= 1
            
            # If no steps left
            if steps == 0:
                jumps += 1
                
                # Cannot move further
                if i >= maxReach:
                    return -1
                
                # Reset steps
                steps = maxReach - i
        
        return -1