# Given a singly linked list, delete the middle of the linked list.

# Note:

# If there are even nodes, then there would be two middle nodes, we need to delete the second middle element.
# If the input linked list has a single node, then it should return NULL.

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteMid(self, head):

        # If list has 0 or 1 node
        if head is None or head.next is None:
            return None

        slow = head
        fast = head
        prev = None

        # Find middle node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete middle node
        prev.next = slow.next

        return head