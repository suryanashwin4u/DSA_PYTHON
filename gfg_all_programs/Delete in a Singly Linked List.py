# You are given the head of a singly linked list and an integer x. 
# Delete the xth node (1-based indexing) from the singly linked list.

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        # Case 1: delete head
        if x == 1:
            return head.next
        
        # Traverse to (x-1)th node
        temp = head
        for _ in range(x - 2):
            temp = temp.next
        
        # Delete xth node
        temp.next = temp.next.next
        
        return head