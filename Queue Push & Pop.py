# Given an array arr[], implement the functions:
# fillQ(): Enqueue all elements of the array into a queue and return the queue.
# emptyQ(): Dequeue all elements from the queue and print them in a single line, separated by spaces, followed by a newline.
# Time Complexity: O(n)
# Auxiliary Space: O(n)

from collections import deque

class Solution:

    def fillQ(self, arr):
        return deque(arr)

    def emptyQ(self, q):
        while q:
            print(q.popleft(), end=" ")
        print()