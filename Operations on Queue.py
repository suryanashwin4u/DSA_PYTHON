# Implement a class myQueue that supports following operations:

# void enqueue(int x): Insert an element x at the end of the queue.
# void dequeue(): Remove the element from the front of the queue.
# int getFront(): Return the element at the front of the queue.
# int getRear(): Return the element at the rear end of the queue.
# bool isEmpty(): Return true if the queue is empty, otherwise false.
# int size(): Return the number of elements currently in the queue.

# There will be a sequence of q queries queries[][]. The queries are represented in numeric form:

# 1 x - Call enqueue(x)
# 2 - Call dequeue()
# 3 - Call getFront()
# 4 - Call getRear()
# 5 - Call isEmpty()
# 6 - Call size()
# The driver code will process the queries, call the corresponding functions, and print the outputs of getFront(), getRear(), isEmpty(), size() operations.
# You only need to implement the above six functions.

class myQueue:
    def __init__(self):
        self.q = []

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if self.q:
            self.q.pop(0)

    def getFront(self):
        if self.q:
            return self.q[0]
        return -1

    def getRear(self):
        if self.q:
            return self.q[-1]
        return -1

    def isEmpty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)