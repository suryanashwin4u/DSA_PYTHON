# Given an array arr, write a program segregating even and odd numbers. 
# The program should put all even numbers first in sorted order, 
# and then odd numbers in sorted order.

# Note:- You don't have to return the array, you have to modify it in-place.

class Solution:
    def segregateEvenOdd(self, arr):
        even = []
        odd = []

        for num in arr:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        even.sort()
        odd.sort()

        arr[:] = even + odd