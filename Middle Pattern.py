# Given an odd length word your task is to complete 
# the function printPattern that takes a string s 
# as its argument and prints it from the middle of the word 
# such that it follows the following pattern.
# Input: PROGRAM 
# Output:
# G$ GR$ GRA$ GRAM$ 
# GRAMP$ GRAMPR$ GRAMPRO$

def printPattern(str):
    n = len(str)
    mid = n // 2
    ls = str[mid:] + str[:mid]
    for i in range(1, n+1):
        print(ls[:i], "$", sep = "", end = " ")
    print()