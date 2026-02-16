# Given an integer n find the sum of the first n natural number.

def nSum(n):
    if n == 0:
        return 0
    return n + nSum(n-1)
