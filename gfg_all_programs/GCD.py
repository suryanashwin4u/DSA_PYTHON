# Given two numbers A and B. 
# The task is to find the GCD of  A and B.
# The GCD of two numbers is the largest number that can divide both A and B perfectly.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a