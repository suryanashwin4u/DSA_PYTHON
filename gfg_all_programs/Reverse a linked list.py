# You are given the head of a singly linked list. 
# You have to reverse the linked list and return the head of the reversed list.

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr is not None:
            next_node = curr.next   # store next node
            curr.next = prev        # reverse link
            prev = curr             # move prev forward
            curr = next_node        # move curr forward
            
        return prev