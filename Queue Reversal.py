# Given a queue q containing integer elements, your task is to reverse the queue.

class Solution:
    def reverseQueue(self, q):
        if not q:
            return
        
        x = q.pop(0)
        self.reverseQueue(q)
        q.append(x)
        
        return q
    
# OR
from collections import deque

class Solution:
    def reverseQueue(self, q):
        stack = []
        
        while len(q) > 0:
            stack.append(q.popleft())
        
        while stack:
            q.append(stack.pop())
        
        return q
# OR
class Solution:
    def reverseQueue(self, q):
        stack = []
        
        # Step 1: Push all elements into stack
        while q:
            stack.append(q.pop(0))   # remove from front
        
        # Step 2: Push back into queue
        while stack:
            q.append(stack.pop())
        
        return q