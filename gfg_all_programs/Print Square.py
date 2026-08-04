# Given an integer s, write a program to print the square of size s using "*" character. 
# Note: Make sure to add a " " between two "*". 
# Add a new line after printing the square

# User function Template for python3
def square(s):
    for i in range(s):
        for j in range(s):
            # print star on boundary
            if i == 0 or i == s-1 or j == 0 or j == s-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print() 