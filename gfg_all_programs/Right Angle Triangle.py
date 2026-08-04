# Given an integer n. Write a program to print the Right angle triangle wall. The length of perpendicular and base is n.  Use single loop and string multiplication.
# Note: Print exactly single " " after "*". Print a new line after printing the triangle.

n = int(input())

for i in range(1, n + 1):
    print("* " * i)