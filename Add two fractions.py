# You are given four numbers num1, den1, num2, and den2. 
# You need to find (num1/den1)+(num2/den2) and output the result in the form of (numx/denx).

def addFraction(num1, den1, num2, den2):

    import math
    
    num = num1*den2 + num2*den1
    den = den1*den2
    
    g = math.gcd(num, den)
    
    print(f"{num//g}/{den//g}")