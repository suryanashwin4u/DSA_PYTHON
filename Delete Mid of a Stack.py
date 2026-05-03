# Given a stack s, delete the middle element of the stack without using any additional data structure.

# Middle element:- floor((size_of_stack+1)/2) (1-based indexing) from the bottom of the stack.

# Note: The output shown by the compiler is the stack from top to bottom.

class Solution:
    def deleteMid(self, stack):

        mid = (len(stack) - 1) // 2

        del stack[mid]