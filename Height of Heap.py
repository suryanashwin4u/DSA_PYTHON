# Given a Binary Heap of size n in an array arr[]. 
# Write a program to calculate the height of the Heap.

# Note: Return 1 if the n is 1.

import math

class Solution:
    def heapHeight(self, n, arr):
        if n == 1:
            return 1
        return int(math.log2(n))

# or simple logic
class Solution:
    def heapHeight(self, n, arr):
        height = -1
        while n > 0:
            n //= 2
            height += 1
        return height