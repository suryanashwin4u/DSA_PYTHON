# Given two circles c1 of radius r1 and c2 of radius r2,centered at (x1,y1) and (x2,y2) respectively. 
# Find out whether they touch(at one or more than one points).

class Solution:
    def circleTouch(self, X1, Y1, R1, X2, Y2, R2):
        # Step 1: Calculate squared distance between centers
        dx = X2 - X1
        dy = Y2 - Y1
        dist_sq = dx*dx + dy*dy
        
        # Step 2: Calculate squared sum of radii
        radius_sum = R1 + R2
        radius_sum_sq = radius_sum * radius_sum
        
        # Step 3: If distance <= sum of radii → circles touch
        if dist_sq <= radius_sum_sq:
            return 1
        else:
            return 0