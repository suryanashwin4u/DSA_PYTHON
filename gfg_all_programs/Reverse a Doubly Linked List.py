# You are given the head of a doubly linked list. You have to reverse the doubly linked list and return its head.

class Solution:
    def reverse(self, head):
        curr = head
        new_head = None
        
        while curr:
            # swap next and prev
            curr.prev, curr.next = curr.next, curr.prev
            
            # update new head
            new_head = curr
            
            # move forward (actually prev after swap)
            curr = curr.prev
        
        return new_head