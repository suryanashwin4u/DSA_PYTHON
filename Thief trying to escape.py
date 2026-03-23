# A thief trying to escape from a jail has to cross N walls 
# whose heights are given in arr[] each with varying heights. 
# He climbs X feet every time. 
# But, due to the slippery nature of those walls, every time he slips back by Y feet.  
# Now the task is to calculate the total number of jumps required to cross all walls 
# and escape from the jail.

class Solution:
    def totalJumps(self, X, Y, N, arr):
        total = 0
        
        for h in arr:
            if X >= h:
                total += 1
            else:
                jumps = (h - X + (X - Y) - 1) // (X - Y) + 1
                total += jumps
        
        return total