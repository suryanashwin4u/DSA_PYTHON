# Given a deque dq containing integer elements, the task is to traverse the dq and print its elements of it. 
# Note: Print a newline at the end.

class Solution:
    def printDeque(self, deq):
        for x in deq:
            print(x, end=" ")
        print()