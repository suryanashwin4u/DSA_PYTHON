# Given a stack of integers and Q queries. 
# The task is to perform the operation on stack according to the query.

# The queries can be of 4 types:
# i x: (adds element x in the stack).
# r: (removes the topmost element from the stack).
# h: Prints the topmost element.
# f y: (check if the element y is present or not in the stack). 
# Print "Yes" if present, else "No". 
class Solution:
    # Function to push an element into the stack.
    def insert(self, s, x):
        s.append(x)

    # Function to remove top element from stack.
    def remove(self, s):
        if len(s) > 0:
            s.pop()

    # Function to print the top element of stack.
    def headOf_Stack(self, s):
        if len(s) > 0:
            print(s[-1])
        else:
            print(-1)

    # Function to search an element in the stack.
    def find(self, s, val):
        return val in s