# Given arrival arr[] and departure dep[] times of trains on the same day, 
# find the minimum number of platforms needed so that no train waits. 
# A platform cannot serve two trains at the same time; 
# if a train arrives before another departs, an extra platform is needed.

# Note: Time intervals are in the 24-hour format (HHMM) , 
# where the first two characters represent hour (between 00 to 23 ) 
# and the last two characters represent minutes (this will be <= 59 and >= 0). 
# Leading zeros for hours less than 10 are optional (e.g., 0900 is the same as 900).


# Time Complexity: O(n log n)
# Auxiliary Space: O(1)

class Solution:
    def minPlatform(self, arr, dep):
        
        arr.sort()
        dep.sort()
        
        i = 0
        j = 0
        
        platforms = 0
        ans = 0
        
        n = len(arr)
        
        while i < n and j < n:
            
            # new train arrives
            if arr[i] <= dep[j]:
                platforms += 1
                ans = max(ans, platforms)
                i += 1
            
            # train departs
            else:
                platforms -= 1
                j += 1
        
        return ans  
