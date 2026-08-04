# Given head of a singly linked list. 
# The task is to find the length of the linked list, 
# where length is defined as the number of nodes in the linked list.

class Solution:
    def getCount(self, head):
        count = 0
        current = head
        
        while current is not None:
            count += 1
            current = current.next
            
        return count
