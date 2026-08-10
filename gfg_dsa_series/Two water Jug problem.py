# You are at the side of a river. 
# You are given a m litre jug and a n litre jug . 
# Both the jugs are initially empty. 
# The jugs dont have markings to allow measuring smaller quantities. 
# You have to use the jugs to measure d litres of water . 
# Determine the minimum no of operations to be performed to obtain d litres of water in one of the jugs.
# The operations you can perform are:

# Empty a Jug
# Fill a Jug
# Pour water from one jug to the other until one of the jugs is either empty or full.


# Time Complexity: O(d)
# Auxiliary Space: O(1)

import math

class Solution:
    def minSteps(self, m, n, d):
        # Target cannot exceed the maximum capacity of both jugs
        if d > max(m, n):
            return -1
        
        # Target must be divisible by the greatest common divisor of m and n
        if d % math.gcd(m, n) != 0:
            return -1
        
        # Helper function to simulate pouring from one jug to another
        def pour(from_cap, to_cap, target):
            from_jug = from_cap
            to_jug = 0
            steps = 1  # Step 1: Fill the source jug
            
            while from_jug != target and to_jug != target:
                # Pour water from_jug -> to_jug until one is full or empty
                temp = min(from_jug, to_cap - to_jug)
                to_jug += temp
                from_jug -= temp
                steps += 1
                
                if from_jug == target or to_jug == target:
                    break
                
                # If source jug becomes empty, fill it up
                if from_jug == 0:
                    from_jug = from_cap
                    steps += 1
                
                # If destination jug becomes full, empty it
                if to_jug == to_cap:
                    to_jug = 0
                    steps += 1
                    
            return steps
        
        # Try both strategies (filling m first vs filling n first) and take the minimum steps
        return min(pour(m, n, d), pour(n, m, d))