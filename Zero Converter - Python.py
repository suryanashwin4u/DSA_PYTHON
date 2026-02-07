# You are given a number n. 
# The number n can be negative or positive. 
# If n is negative, print numbers from n to 0 by adding 1 to n in the neg function. 
# If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.

# Note:- You don't have to return anything, you just have to print the array.

def pos(n):
    # Case when n is zero
    if n == 0:
        print("already Zero")
        return
    
    # Print from n-1 down to 0
    while n > 0:
        print(n-1, end=" ")
        n -= 1

def neg(n):
    # Case when n is zero
    if n == 0:
        print("already Zero")
        return
    
    # Print from n up to 0
    while n <= 0:
        print(n, end=" ")
        n += 1