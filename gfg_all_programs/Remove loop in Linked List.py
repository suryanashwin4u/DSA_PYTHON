# Given the head of a singly linked list, 
# the task is to remove a cycle if present. 
# A cycle exists when a node's next pointer points back to a previous node, forming a loop. 
# Internally, a variable pos denotes the index of the node where the cycle starts, 
# but it is not passed as a parameter. 
# The terminal will print true if a cycle is removed otherwise, it will print false.

'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    def removeLoop(self, head):
        if not head or not head.next:
            return
        
        slow = head
        fast = head
        
        # Step 1: Detect loop
        loop_exists = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                loop_exists = True
                break
        
        if not loop_exists:
            return
        
        # Step 2: Find start of loop
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        # Step 3: Find last node of loop
        temp = slow
        while temp.next != slow:
            temp = temp.next
        
        # Break loop
        temp.next = None