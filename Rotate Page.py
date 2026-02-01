# You are given three points a(a1, a2), b(b1, b2) and c(c1, c2) on a page. 
# Find if it’s possible to rotate the page in any direction by any angle, 
# such that the new position of a is same as the old position of b, 
# and the new position of b is same as the old position of c. 

class Solution:
    def possibleOrNot(self, a1, a2, b1, b2, c1, c2):
        # Calculate squared distance between point a and point b
        # (We use squared distance to avoid using sqrt)
        dist_ab = (a1 - b1) ** 2 + (a2 - b2) ** 2
        
        # Calculate squared distance between point b and point c
        dist_bc = (c1 - b1) ** 2 + (c2 - b2) ** 2
        
        # If both distances are equal, rotation is possible
        if dist_ab == dist_bc:
            return 1
        else:
            return 0


