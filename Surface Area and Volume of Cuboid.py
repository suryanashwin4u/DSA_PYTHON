# Given length l, width b and height h of a cuboid. 
# Your task is to return an array containing the total surface area and volume of the cuboid.

class Solution:
    def find(self, l, b, h):
        surface_area = 2 * (l*b + b*h + l*h)
        volume = l * b * h
        return [surface_area, volume]