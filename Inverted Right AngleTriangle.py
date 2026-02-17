# Given an integer n. 
# Write a program to print the inverted "Right angle triangle" wall. 
# The length of the perpendicular and base is n.
# Note: Use string multiplication for python.
# Input: n = 4
# Output:
# * * * * 
# * * * 
# * * 
# *


class Solution:
    def printPattern(self, n):
        for i in range(n, 0, -1):   # start from n down to 1
            print("* " * i)         # print i stars

