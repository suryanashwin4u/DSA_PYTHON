# You are given an array of a fixed size. 
# Your task is to efficiently implement two stacks in this single array.

# The following operations must be supported:

# (i) twoStacks : Initialize the data structures and variables to be used to implement  2 stacks in one array.
# (ii) push1(x) : pushes element into the first stack.
# (iii) push2(x) : pushes element into the second stack.
# (iv) pop1() : pops an element from the first stack and returns the popped element. 
# If the first stack is empty, it should return -1.
# (v) pop2() : pops an element from the second stack and returns the popped element. 
# If the second stack is empty, it should return -1.

class TwoStacks:
    
    def __init__(self, n=100):
        self.size = n
        self.arr = [0] * n
        
        self.top1 = -1
        self.top2 = n

    # Push in stack 1
    def push1(self, x):

        if self.top1 + 1 < self.top2:
            self.top1 += 1
            self.arr[self.top1] = x

    # Push in stack 2
    def push2(self, x):

        if self.top1 + 1 < self.top2:
            self.top2 -= 1
            self.arr[self.top2] = x

    # Pop from stack 1
    def pop1(self):

        if self.top1 == -1:
            return -1

        val = self.arr[self.top1]
        self.top1 -= 1

        return val

    # Pop from stack 2
    def pop2(self):

        if self.top2 == self.size:
            return -1

        val = self.arr[self.top2]
        self.top2 += 1

        return val