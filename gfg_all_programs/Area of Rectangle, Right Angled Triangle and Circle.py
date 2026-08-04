# Given the length of rectangle, 
# width of rectangle, 
# base of right angled triangle, 
# perpendicular of right angled triangle 
# and radius of circle respectively. 
# Calculate the area of rectangle, 
# right angled triangle and 
# circle.

class Solution:
    def getAreas(self, L, W, B, H, R):
        # Area of rectangle = Length × Width
        rect_area = L * W
        
        # Area of right-angled triangle = 0.5 × Base × Height
        tri_area = int(0.5 * B * H)
        
        # Area of circle = 3.14 × R × R
        cir_area = int(3.14 * R * R)
        
        # Return all three areas in a list
        return [rect_area, tri_area, cir_area]