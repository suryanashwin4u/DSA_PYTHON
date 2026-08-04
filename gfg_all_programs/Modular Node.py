# Given the head of a Singly Linked List and a number k, the task is to find the data of the modular node of the linked list. If no such index is present return -1.
# A modular node is defined as the last node in the linked list whose index is divisible by k (i%k==0). 
# Note: 1-based indexing is followed

class Solution:
    def modularNode(self, head, k):
        index = 1
        answer = -1
        
        curr = head
        
        while curr:
            if index % k == 0:
                answer = curr.data
            
            curr = curr.next
            index += 1
        
        return answer