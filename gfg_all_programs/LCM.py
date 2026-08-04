# Given two numbers a and b. The task is to find out their LCM.

#User function Template for python3

def LCM(a, b):
    
    # function to calculate GCD using Euclid algorithm
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x
    
    # return LCM using formula
    return (a * b) // gcd(a, b)