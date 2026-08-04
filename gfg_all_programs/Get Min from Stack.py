# Implement a class SpecialStack that supports following operations:

# push(x) – Insert an integer x into the stack.
# pop() – Remove the top element from the stack.
# peek() – Return the top element from the stack. If the stack is empty, return -1.
# getMin() – Retrieve the minimum element from the stack in O(1) time. If the stack is empty, return -1.
# isEmpty() –  Return true if stack is empty, else false
# There will be a sequence of queries queries[][]. The queries are represented in numeric form:

# 1 x : Call push(x)
# 2:  Call pop()
# 3: Call peek()
# 4: Call getMin()
# 5: Call isEmpty()
# The driver code will process the queries, call the corresponding functions, and print the outputs of peek(), getMin(), isEmpty() operations.
# You only need to implement the above five functions.

# Time Complexity: O(1)
# Auxiliary Space: O(1)

class SpecialStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x):
        self.stack.append(x)

        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self):
        if not self.stack:
            return

        top = self.stack.pop()

        if top == self.minStack[-1]:
            self.minStack.pop()

    def peek(self):
        if not self.stack:
            return -1

        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def getMin(self):
        if not self.minStack:
            return -1

        return self.minStack[-1]