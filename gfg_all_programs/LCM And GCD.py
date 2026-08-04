# Given two integers a and b, 
# You have to compute their LCM and GCD and return an array containing their LCM and GCD.

class Solution:
    def lcmAndGcd(self, a: int, b: int):
        x, y = a, b
        
        # Find GCD using Euclidean Algorithm
        while y != 0:
            x, y = y, x % y
        
        gcd = x
        
        # Find LCM using formula
        lcm = (a * b) // gcd
        
        return [lcm, gcd]
