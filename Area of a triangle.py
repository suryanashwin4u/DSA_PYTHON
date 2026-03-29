# Given three sides of a triangle A, B and C in the form of integers. Find the area of the triangle.
# Note: The triangle may not exist. In such cases, the area is 0.

import math

class Solution:
    def findArea(self, A, B, C):
        # Check triangle validity
        if A + B <= C or B + C <= A or C + A <= B:
            return 0.000
        
        # Semi-perimeter
        s = (A + B + C) / 2
        
        # Heron's formula
        area = math.sqrt(s * (s - A) * (s - B) * (s - C))
        
        return round(area, 3)
