# Given an array arr[] , enqueue the elements of the array into a queue and then dequeue them.

from collections import deque

class Solution:
    
    def fillQ(self, arr):
        q = deque()
        for x in arr:
            q.append(x)   # enqueue
        return q

    def emptyQ(self, q):
        while q:
            print(q.popleft(), end=" ")   # dequeue