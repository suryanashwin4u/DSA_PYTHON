# Given a quadratic equation ax2 + bx + c = 0, find its roots. 
# If the equation has real roots, then return floor value of each root in decreasing order, 
# If the roots are imaginary return -1, the driver code will print Imaginary.
# Time Complexity: O(1)
# Auxiliary Space: O(1)

from math import sqrt, floor

class Solution:
    def quadraticRoots(self, a: int, b: int, c: int):
        
        d = (b * b) - (4 * a * c)
        
        # Imaginary roots
        if d < 0:
            return [-1]
        
        r1 = (-b + sqrt(d)) / (2 * a)
        r2 = (-b - sqrt(d)) / (2 * a)
        
        r1 = floor(r1)
        r2 = floor(r2)
        
        # Return in decreasing order
        if r1 >= r2:
            return [r1, r2]
        else:
            return [r2, r1]

