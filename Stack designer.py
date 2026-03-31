# You are given an integer array arr[]. 
# You need to push the elements of the array into a stack and then print them while popping.
# Note: No need to print extra line after printing the stack elements.

class Solution:
    
    def _push(self, arr):
        return arr[:]   # stack is just a list copy

    def _pop(self, stack):
        while stack:
            print(stack.pop(), end=' ')