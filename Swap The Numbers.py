# Given two numbers a and b, 
# you need to swap their values so a holds the value of b and b holds the value of a. 
# Just write the code to swap values of a and b at the specified place.

a = int(input())
b = int(input())
a, b = b, a
print(a, b)

# or

class Solution:
    def swap(self, a, b):
        a, b = b, a
        print(a, b)