# Find the focal length of the spherical mirror with the given radius-of-curvature R.

import math

class Solution:
    def findFocalLength(self, R, type):
        # If mirror is concave
        if type == "concave":
            # Focal length = floor(R / 2)
            return math.floor(R / 2)
        
        # If mirror is convex
        else:
            # Focal length = floor(-R / 2)
            return math.floor(-R / 2)