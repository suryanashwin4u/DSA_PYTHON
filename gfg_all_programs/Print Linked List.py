# Given the head of a singly linked list. The task is to print the linked list.

class Solution:
    def displayList(self, head):
        result = []
        
        current = head
        while current is not None:
            result.append(current.data)
            current = current.next
        
        return result