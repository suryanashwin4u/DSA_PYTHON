# You are given the head of a linked list, You have to return the value of the middle node of the linked list.

# If the number of nodes is odd, return the middle node value.
# If the number of nodes is even, there are two middle nodes, so return the second middle node value

class Solution:
    def getMiddle(self, head):
        if head is None:
            return -1
        
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data