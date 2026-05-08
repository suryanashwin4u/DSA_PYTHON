# Implement a Queue using 2 stacks s1 and s2 .
# A Query q is of 2 Types
# (i) 1 x (a query of this type means  pushing 'x' into the queue)
# (ii) 2   (a query of this type means to pop element from queue and print the poped element)

# Note : If there is no element return -1 as answer while popping.

#User function Template for python3

class StackQueue:
    
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, B):
        self.s1.append(B)

    def pop(self):
        
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        
        if not self.s2:
            return -1
        
        return self.s2.pop()