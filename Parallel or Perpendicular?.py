# Given two force vectors, find out whether they are parallel, perpendicular or neither. 
# Let the first vector be A = a1 i +a2 j + a3 k 
# and 
# the second vector be B = b1 i + b2 j + b3 k.
# A.B = a1 * b1 + a2 * b2 + a3 * b3
# A x B = (a2 * b3 - a3 * b2) i - (a1 * b3 - b1* a3) j + (a1 * b2 - a2 * b1) k
# |A|2 = a12 + a22 + a32
# If A.B = 0, then A and B are perpendicular.
# If |A X B|2 = 0, then A and B are parallel.

class Solution:
    def find(self, A, B):
        a1, a2, a3 = A
        b1, b2, b3 = B
        
        # Step 1: Calculate dot product
        dot = a1*b1 + a2*b2 + a3*b3
        
        # If dot product is zero → perpendicular
        if dot == 0:
            return 2
        
        # Step 2: Calculate cross product components
        cx = a2*b3 - a3*b2
        cy = a1*b3 - a3*b1
        cz = a1*b2 - a2*b1
        
        # If cross product magnitude squared is zero → parallel
        if cx*cx + cy*cy + cz*cz == 0:
            return 1
        
        # Otherwise
        return 0